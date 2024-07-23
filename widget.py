# This Python file uses the following encoding: utf-8
import sys
import numpy as np
from numpy import f2py
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
import scipy.signal as signal

from PySide6.QtWidgets import QApplication, QWidget
from ui_form import Ui_Widget
from PySide6 import QtCore

QTIM_DELAY = 1000

#Matplotlib Config Style
background_color = '#2b2130'
text_color = '#FFFFFF'

plt.rcParams.update({
    'axes.facecolor': background_color, 
    'axes.edgecolor': text_color,  
    'axes.labelcolor': text_color, 
    'xtick.color': text_color, 
    'ytick.color': text_color,  # Color de las marcas del eje y
    'text.color': text_color,  # Color del texto general
    'figure.facecolor': background_color,  # Color de fondo de la figura
    'figure.edgecolor': background_color,  # Color del borde de la figura
    'grid.color': text_color,  # Color de la cuadrícula
    'grid.linestyle': '--',  # Estilo de la línea de la cuadrícula
    'grid.linewidth': 0.5,  # Ancho de línea de la cuadrícula
    'legend.facecolor': background_color,  # Color de fondo de la leyenda
    'legend.edgecolor': text_color,  # Color del borde de la leyenda
    'font.size' : 9 #tamaño de fuente
})
colors = [(0.2980392156862745, 0.4470588235294118, 0.6901960784313725), 
          (0.8666666666666667, 0.5176470588235295, 0.3215686274509804), 
          (0.3333333333333333, 0.6588235294117647, 0.40784313725490196), 
          (0.7686274509803922, 0.3058823529411765, 0.3215686274509804), 
          (0.5058823529411764, 0.4470588235294118, 0.7019607843137254), 
          (0.5764705882352941, 0.47058823529411764, 0.3764705882352941), 
          (0.8549019607843137, 0.5450980392156862, 0.7647058823529411), 
          (0.5490196078431373, 0.5490196078431373, 0.5490196078431373), 
          (0.8, 0.7254901960784313, 0.4549019607843137), 
          (0.39215686274509803, 0.7098039215686275, 0.803921568627451)]


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.debug = False

   

        #QTimer_ini
        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.main_sequence)

        
        self.SnrValues = [x*5 for x in range(11)]
        self.QuantizationValues = [2**x for x in range(0, 9)]
        self.ui.compression_factor.clear()
        self.ui.compression_factor.addItems(['1', '10', '100', '200', '400', '700'])

        #User input 

        #Display Dial Data on GUI lcd
        self.ui.snr_knob.valueChanged.connect(self.update_snr_lcd)
        self.ui.quantization_knob.valueChanged.connect(self.update_quantization_lcd)

        self.snr = self.ui.snr_knob.value()
        self.q_levels = self.ui.quantization_knob.value()
        
        # Execute on Event:
        self.update_quantization_lcd(self.q_levels)
        self.update_snr_lcd(self.snr)
        self.ui.update.clicked.connect(self.schedule_plot_update)

    
       
        


    def sample_user_data(self):
        self.amplitude = self.ui.amplitude.value()
        self.signal_frequency = self.ui.frequency.value()
        self.time_span = (self.ui.duration.value() / 1000)
        self.sampling_factor = self.ui.sampling_factor.value()
        self.wave_type = self.ui.wave_type_dropdown.currentIndex()
        self.freq_factor = self.ui.freq_separation_factor.value()
        self.compression_type = self.ui.compression_type.currentIndex()
        self.compression_factor = int(self.ui.compression_factor.currentText())
        self.q_levels = self.ui.quantization_knob.value()
        self.channel_code = self.ui.channel_cod_dropdown.currentIndex()

        #update ui
        self.ui.duration.setMinimum(-(3.9/self.signal_frequency) * 1000)
        self.ui.duration.setMaximum((3.9/self.signal_frequency) * 1000)       

        self.dsp = DSP(self.signal_frequency,
                       self.sampling_factor, 
                       self.SnrValues, 
                       self.QuantizationValues,
                       self.debug)


    def schedule_plot_update(self):
        self.timer.start(QTIM_DELAY)

    def update_quantization_lcd(self, value):
        mapped_val = self.QuantizationValues[value]
        self.ui.quantization_display.display(mapped_val)

    def update_snr_lcd(self, value):
        mapped_val = self.SnrValues[value]
        self.snr = mapped_val
        self.ui.snr_display.display(mapped_val)

    def main_sequence(self):
        self.sample_user_data()

        time_sv, user_signal = self.dsp.wave_generator(self.wave_type, self.amplitude, self.freq_factor)
        discrete_sv, sampled_signal = self.dsp.sampler(user_signal)
        sig_compressed = self.dsp.compressor(sampled_signal, self.compression_factor, self.compression_type)
        Quant, bin_sig = self.dsp.quantizer(sig_compressed, self.q_levels)
        zero_filled = self.dsp.zero_fill(time_sv, sampled_signal)
        print(len(sampled_signal))
        freq_sv, freq_c_signal = self.dsp.get_spectrum(time_sv, user_signal)
        freq_d_signal = self.dsp.get_spectrum(discrete_sv, zero_filled)[1]

        bit_rate = int(self.q_levels*((self.dsp.fs)))
        t_sv, bits = self.encodig(bin_sig, self.channel_code, bit_rate)


        self.create_compression_graph()        
        self.clear_layout(self.ui.Signal_Tiempo)

        

        fig, ax = plt.subplots(figsize=(12,4))
        ax.plot(time_sv, user_signal, 
                linewidth=2, 
                label="Señal Analógica", 
                color=colors[1])
        ax.stem(discrete_sv, sampled_signal, 
                linefmt = 'y--',
                markerfmt = 'yx',
                basefmt=" ",
                label='Señal Muestreada')
        ax.scatter(discrete_sv, Quant, 
                   color=colors[0], 
                   label='Señal Cuantizada',
                   alpha = 1,
                   zorder = 2)
        ax.legend(loc='upper right', fontsize=8, shadow=False)        
        ax.set_title("m(t), m[n] y Q[n]")
        ax.set_ylabel("A")
        ax.set_xlabel("t")
        ax.grid()
        ax.axis([0, 4/self.signal_frequency + self.time_span, -1.1*self.dsp.Vp_analog, +1.1*self.dsp.Vp_analog])       
        fig.tight_layout()

        canvas = FigureCanvas(fig)
        self.ui.Signal_Tiempo.addWidget(canvas)
        plt.close(fig)      

        self.create_plot(freq_sv, freq_c_signal,
                         'PSD Banda Base', 'f', 'A', None, 
                         self.ui.BaseBand_Freq, 
                         colors[1], 
                         None, 
                         0, 
                         [-15*self.signal_frequency, 15*self.signal_frequency, 0, 0.7*self.amplitude])
        self.create_plot(freq_sv, freq_d_signal, 
                         'PSD Banda Base', 'f', 'A', None, 
                         self.ui.Quantized_Freq, 
                         colors[1], 
                         None, 
                         0, 
                         [-15*self.signal_frequency, 15*self.signal_frequency, 0, 0.7*self.amplitude])
    
        self.display_PCM_codes('bits.txt', self.ui.PCM_OUT)

        
        self.create_plot(t_sv, bits, 
                         'Codificacion de Linea', 't', 'A', None,
                         self.ui.Mod_Tiempo, 
                         colors[1],
                         None, 
                         0,
                         plot_axis=[0, 4/self.signal_frequency + self.time_span, -1.2 ,1.2])
        
        #paso por el canal


        freq_sv, bits_spec = self.dsp.get_spectrum(t_sv, bits)
        bits_db = 10*np.log10((bits_spec)**2)
        
        self.create_plot(freq_sv, bits_db, 
                         'Espectro Señal', 'f', 'dB', None,
                         self.ui.Mod_Freq, 
                         colors[1], plot_axis=[-5e3, 5e3, -100, -20],
                         linewidth=0.5,
                         minor_gridlines=True)
        

        bits_noise = self.dsp.awgn(self.snr, bits)

        bits_noise_spec = 10*np.log10(self.dsp.get_spectrum(t_sv, bits_noise)[1] ** 2)
        
        self.create_plot(t_sv, bits_noise, 
                         'Señal en presencia de ruido', 't', 'A', None,
                         self.ui.AWGN_Tiempo, 
                         colors[1], 
                         plot_axis=[0, 4/self.signal_frequency + self.time_span, -1.2 ,1.2])
         
        self.create_plot(freq_sv, bits_noise_spec, 
                         'Espectro Señal', 'f', 'dB', None,
                         self.ui.AWGN_Freq, 
                         colors[1], plot_axis=[-5e3, 5e3, -100, -20],
                         linewidth=0.5,
                         minor_gridlines=True)
        #recepcion y deteccion

        filtered_bits = self.dsp.LPF(self.dsp.fs / 32, bits_noise)

        filtered_bits_spec = 10*np.log10(self.dsp.get_spectrum(t_sv, filtered_bits) [1] ** 2)

        self.create_plot(freq_sv, filtered_bits_spec, 
                         'Señal Recibida Filtrada', 'f', 'dB', None,
                         self.ui.H_Filtro, 
                         colors[1], plot_axis=[-5e3, 5e3, -100, -20],
                         linewidth=0.5,
                         minor_gridlines=True)
        
        
        decoded_bits, t_s, s_s = self.decodig(filtered_bits, t_sv, self.channel_code, bit_rate, 30)
            
        reconstructed_sample = self.dsp.recontructor(decoded_bits, self.q_levels)
        print(len(reconstructed_sample))
        m_prime_x = self.dsp.zero_order_hold(time_sv, reconstructed_sample)

        mprime_f_SV, m_prime_spec = self.dsp.get_spectrum(time_sv, m_prime_x)


        self.create_plot(time_sv, m_prime_x, 
                         "Señal Reconstruida", 
                         't', 'A', None,
                         self.ui.Signal_ZOH, 
                         color= colors[1],
                         plot_type = 0,
                         plot_axis=[0, 4/self.signal_frequency + self.time_span, -1.1*self.dsp.Vp_analog, +1.1*self.dsp.Vp_analog])
        
        self.create_plot(mprime_f_SV, m_prime_spec, 
                         'PSD Señal Reconstruida', 'f', 'A', None, 
                         self.ui.Spec_ZOH, 
                         colors[1], 
                         None, 
                         0, 
                         [-15*self.signal_frequency, 15*self.signal_frequency, 0, 0.7*self.amplitude])

        self.display_PCM_codes('rx_bits.txt', self.ui.PCM_RX)
        self.clear_layout(self.ui.Signal_Dec)

        

        fig, ax = plt.subplots()
        ax.plot(t_sv, filtered_bits, 
                linewidth=2, 
                label="Señal Recibida", 
                color=colors[1])
        ax.stem(t_s, s_s, 
                linefmt = 'y--',
                markerfmt = 'yx',
                basefmt=" ",
                label='Muestras en Señal')
        
        ax.legend(loc='upper right', fontsize=8, shadow=False)        
        ax.set_title("Recepcion y Muestreo")
        ax.set_ylabel("A")
        ax.set_xlabel("t")
        ax.grid()
        ax.axis([0, 4/self.signal_frequency + self.time_span, -1.1*self.dsp.Vp_analog, +1.1*self.dsp.Vp_analog])       
        fig.tight_layout()

        canvas = FigureCanvas(fig)
        self.ui.Signal_Dec.addWidget(canvas)
        plt.close(fig)      
        


        
    
    def encodig(self, bin_signal, encoding, bit_rate):
        if encoding == 0:
            x, y = self.dsp.NRZ_enc(bin_signal, bit_rate, 1)
            return x, y
        elif encoding == 1:
            x, y = self.dsp.RZ_enc(bin_signal, bit_rate, 1)
            return x, y
        elif encoding == 2:
            x, y = self.dsp.RZ_AMI_enc(bin_signal, bit_rate, 1)
            return x, y
    
    def decodig(self, rx_signal, time_vector, encoding, bit_rate,shift):
        if encoding == 0:
            bits, t_s, s_s = self.dsp.NRZ_dec(time_vector, rx_signal, bit_rate, shift)
            return bits, t_s, s_s
        elif encoding == 1:
            bits, t_s, s_s = self.dsp.RZ_dec(time_vector, rx_signal, bit_rate , shift)
            return bits, t_s, s_s
        elif encoding == 2:
            bits, t_s, s_s = self.dsp.RZ_AMI_dec(time_vector, rx_signal, bit_rate, shift)
            return bits, t_s, s_s
        
        pass
    
    
    def create_plot(self, x_axis, y_axis, 
                    line_label, x_label, y_label, 
                    title, widget_identifier, color, 
                    plot_size=None, 
                    plot_type=0,
                    plot_axis = None,
                    plot_xlim = None,
                    plot_ylim = None,
                    linewidth = None,
                    minor_gridlines = False,
                    no_tick_labels = False):
        
        self.clear_layout(widget_identifier)

        fig, ax = plt.subplots(figsize = plot_size)

        if plot_type == 0:
            ax.plot(x_axis, y_axis, color=color, label=line_label, linewidth=linewidth)
        elif plot_type == 1:
            ax.stem(x_axis, y_axis, 'r*', label=line_label, basefmt=" ")
        elif plot_type == 2:
            ax.scatter(x_axis, y_axis, color=color, label=line_label)
        
        ax.set_title(title, fontsize=8)
        ax.set_ylabel(y_label)
        ax.set_xlabel(x_label)
        ax.set_xlim(plot_xlim)
        ax.set_ylim(plot_ylim)

        if minor_gridlines:
            ax.grid(True, which='major', linestyle='-')
            ax.grid(True, which='minor', linestyle=':')
            ax.minorticks_on()
        else:
            ax.grid()

        if no_tick_labels:
            ax.set_xticklabels([])
            ax.set_yticklabels([])

        ax.legend(loc='upper right', fontsize=10, shadow=False)  
        ax.axis(plot_axis)
        fig.tight_layout()

        canvas = FigureCanvas(fig)
        widget_identifier.addWidget(canvas)

        plt.close(fig)
    

    
    def display_PCM_codes(self, file, widget_identifier):
        filename = file
        with open(filename, "r") as file:
            lines = []
            try:
                for _ in range(20):
                    lines.append(next(file))
            except StopIteration:
                pass

            contents = ''.join(lines)
            widget_identifier.setPlainText(contents)    
        

    def clear_layout(self, layout):
         while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def create_compression_graph(self):
        n = np.linspace(-1, 1, 100)
        if self.compression_type == 0:
            n_law = n
        else:
            n_law = self.dsp.compressor(n, self.compression_factor, self.compression_type)

        self.create_plot(n, n_law, 
                         "Compresion Aplicada", 
                         None, None, None, 
                         self.ui.Compression_Graph, 
                         colors[-1], (3, 3), 
                         plot_axis=[-1, 1, -1, 1],
                         no_tick_labels=True)



class DSP:
    def __init__(self, f, k, snr_values, quantization_values, debug):
        #time domain
        self.f = f
        self.dt = 1 / (1000*self.f)
        self.t = np.arange(0, 20/self.f, self.dt)

        #Discrete time domain
        self.k = k
        self.fs = self.k * (2 * self.f) #Frecuencia de muestreo   
        self.sf = round((1 / self.fs) / self.dt) #escalon de muestreo discreto
        #noise
        self.Vp = None
        self.Vp_analog = None
        self.snr = snr_values
        self.quantization_values = quantization_values
        self.debug = debug
    
    def wave_generator(self, wave_type, A, variablility_factor):
 
        coef_A = (1 + 0.4 * variablility_factor)
        coef_B = (1 + 0.2 * variablility_factor)

        if wave_type == 0:
            signal_vector = A*np.sin(2 * np.pi * self.f * self.t)
        elif wave_type == 1:
            signal_vector = A*signal.sawtooth(2 * np.pi * self.f * self.t, 0.5)
        elif wave_type == 2:
            signal_vector = A*signal.square(2 * np.pi * self.f * self.t)
        elif wave_type == 3:
            signal_vector = A*signal.sawtooth(2 * np.pi * self.f * self.t)
        elif wave_type == 4:
            signal_vector = A*(np.cos(coef_B * 2 * np.pi * self.f * self.t + np.pi / 3) + 
                               coef_A*np.sin(2 * np.pi * 2 * self.f * self.t + np.pi / 4)) / 2
        elif wave_type == 5:
            signal_vector = A*(coef_B* np.sin(coef_A*2 * np.pi * self.f * self.t) +
                             coef_A* np.sin(coef_B*4 * np.pi * self.f * self.t) +
                             np.sin(coef_B*6 * np.pi * self.f * self.t)) / 3
        else:
            raise ValueError("Unsupported wave type")
        
        self.Vp_analog = max(abs(signal_vector))

        return self.t, signal_vector
    
    def compressor(self, signal, factor, law=None, inv=False):
        self.Vp = np.max(abs(signal))
        norm_sig = signal / self.Vp #min-max normalization

        if law == 0:
            return signal
        
        elif law == 1:
            #Mulaw
            if not inv:
                #no inversa 
                sign = np.ones(len(norm_sig))
                sign[norm_sig <= 0] = -1
                y = (1 / np.log(1 + factor)) * np.log(1 + factor * np.abs(norm_sig)) * sign
                return y * self.Vp #denormalization
            else:
                #inversa
                sign = np.ones(len(y))
                sign[norm_sig <= 0] = -1
                x = (np.exp(np.abs(y) * np.log(1 + factor)) - 1) / factor * sign
                return x * self.Vp #denormalization
            
        elif law == 2 :
            #A-law
            if not inv:
                #No inversa
                C = np.zeros_like(norm_sig, dtype=float)
                for i in range(len(norm_sig)):
                    abs_val = np.abs(norm_sig[i])
                    if 0 < abs_val <= 1 / factor: #factor being A
                        C[i] = factor * abs_val / (1 + np.log(factor))
                    elif 1 / factor < abs_val <= 1:
                        C[i] = (1 + np.log(factor * abs_val)) / (1 + np.log(factor))
                
                C = C * np.sign(norm_sig) * self.Vp #Denormalization
                return C
            else:
                C = np.zeros_like(norm_sig, dtype=float)
                for i in range(len(norm_sig)):
                    abs_val = np.abs(norm_sig[i])
                    if 0 < abs_val <= 1 / (1 + np.log(factor)):
                        C[i] = (abs_val * (1 + np.log(factor))) / factor
                    elif 1 / (1 + np.log(factor)) < abs_val <= 1:
                        C[i] = np.exp(abs_val * (1 + np.log(factor)) - 1) / factor

                C = C * np.sign(norm_sig) * self.Vp #denormalization
                return C
    
    def sampler(self, signal):
        sampled_signal = signal[::self.sf]
        discrete_time_support_vector = self.t[::self.sf]

        return discrete_time_support_vector, sampled_signal

    def zero_fill(self, time_vector, discrete_signal):
        zero_filled = np.zeros(len(time_vector))
        zero_filled[::self.sf] = discrete_signal
        return zero_filled
    
    def zero_order_hold(self, time_vector, discrete_signal):
        zero_filled = self.zero_fill(time_vector, discrete_signal)
        for i in range(1, len(zero_filled)):
            if zero_filled[i] == 0:  
                zero_filled[i] = zero_filled[i - 1]
    
        return zero_filled
    
    def quantizer(self, signal ,l):
        
        Vp = max(abs(signal))
        DR = 2*Vp
        L = 2 ** l #step numbert, l = btis per word
        q = DR / L  
        x = np.copy(signal)
        x[x > Vp] = Vp - q / 2  # saturation
        x[x < -Vp] = -Vp + q  / 2   
        Q = q * (np.floor(x / q))
        nivel = ((Q - q / 2) / q + (L / 2)).astype(np.uint8)

        self.num_samples = len(signal)

        if self.debug:
            # Debugging outputs to verify ranges
            print(f"Input bit width (l): {l}")
            print(f"DEBUG: Max value in signal: {max(signal)}")
            print(f"DEBUG: Min value in signal: {min(signal)}")
            print(f"DEBUG: Max value in Q: {max(Q)}")
            print(f"DEBUG: Min value in Q: {min(Q)}")
            print(f"DEBUG: Max value in nivel: {max(nivel)}")
            print(f"DEBUG: Min value in nivel: {min(nivel)}")
        
        cod = np.array([np.binary_repr(n, width=l) for n in nivel])

        cat_cod = ''.join(cod)
        bin_cod = np.array(list(cat_cod)).astype(int)

        ### Save decoded bits

        with open("bits.txt", "w") as file:
            file.write(f"{'':>12}Bits Transmitidos \n")
            file.write(f"{'x(t)':>10} {'Q(x)':>10} {'Nivel':>6} {'PCMcode':>9}\n")
            for i in range(len(x)):
                file.write(f"{str(f'{x[i]:8.6f}'):>10} {str(f'{Q[i]:8.6f}'):>10} {str(f'{nivel[i]:3d}'):>6} {str(f'{cod[i]:6s}'):>9}\n")
            
            file.write("\n")
        
        return Q, bin_cod
    
    def recontructor(self, bits, l):
        Vp = self.Vp
        DR = 2 * Vp
        L = 2 ** l  
        q = DR / L  
        bit_groups = [bits[i:i+l] for i in range(0, len(bits), l)]
        bit_values = [int(''.join(map(str, group)), 2) for group in bit_groups]
        niveles = np.arange(L) 
        x = (niveles[bit_values] - (L / 2)) * q + q / 2

        x = x[:self.num_samples] 

        if self.debug:
            # Debugging outputs to verify ranges
            print(f"DEBUG: Start Reconstructor")
            print(f"DEBUG: output bit width (l): {l}")
            print(f"DEBUG: Max value in signal: {max(x)}")
            print(f"DEBUG: Min value in signal: {min(x)}")

            print(f"DEBUG: Max value in nivel: {max(niveles)}")
            print(f"DEBUG: Min value in nivel: {min(niveles)}")
        
    
        with open("rx_bits.txt", "w") as file:
            file.write(f"{'':>8}Bits Recibidos \n")
            file.write(f"{'x_prima(t)':>10} {'Nivel':>6} {'PCMcode':>9}\n")
            for i in range(len(x)):
                bit_group_str = ''.join(map(str, bit_groups[i]))  # Convert list to string
                file.write(f"{str(f'{x[i]:8.6f}'):>10} {str(f'{bit_values[i]:3d}'):>6} {bit_group_str:>9}\n")
            file.write("\n")

        return x




    def get_spectrum(self, support_vector, signal):
        S = np.fft.fftshift(np.abs(np.fft.fft(signal)) / len(support_vector))
        Fs = 1 / self.dt
        freq_sv = np.linspace(-np.floor(Fs / 2), np.ceil(Fs / 2), len(signal))
    
        return freq_sv, S
    
    #Encoding and decoding functions    
    def RZ_enc(self, h, bit_rate, duracion):
        n_bits = len(h)
        t_bit = 1 / bit_rate
        t_s = np.arange(0, duracion, t_bit / 100)  # Vector Tiempo
        s_s = np.zeros(len(t_s))  # Iniciar salida
        
        for i in range(n_bits):
            bit_i = i * t_bit  # Start current bit time
            bit_f = (i + 1) * t_bit - 0.5 * t_bit  # End current bit time
        
            if h[i] == 1:
                s_s[(t_s >= bit_i) & (t_s <= bit_f)] = 1  # High voltage condition
            else:
                s_s[(t_s >= bit_i) & (t_s <= bit_f)] = -1  # Low voltage condition
        
        return t_s, s_s

    def NRZ_enc(self, h, bit_rate, duracion):
        n_bits = len(h)
        t_bit = 1 / bit_rate
        t_s = np.arange(0, duracion, t_bit / 100)  # Support Vector
        s_s = np.zeros(len(t_s))  # initialize output
        
        for i in range(n_bits):
            bit_i = i * t_bit  # Start current bit time
            bit_f = (i + 1) * t_bit  # end current bit time
        
            if h[i] == 1:
                s_s[(t_s >= bit_i) & (t_s <= bit_f)] = 1  # High voltage condition
            else:
                s_s[(t_s >= bit_i) & (t_s <= bit_f)] = 0  # Low voltage condition
        
        return t_s, s_s

    def RZ_AMI_enc(self, h, bit_rate, duracion):
        n_bits = len(h)
        t_bit = 1 / bit_rate
        t_s = np.arange(0, duracion, t_bit / 100)  # Time vector
        s_s = np.zeros(len(t_s))  # Initialize output signal
        ultima_polaridad = -1  # Variable to store last polarity (-1 for initial state)
        
        for i in range(n_bits):
            bit_i = i * t_bit  # Start time of the current bit
            bit_f = (i + 1) * t_bit  # End time of the current bit
            
            if h[i] == 1:
                ultima_polaridad *= -1  # Invert polarity
                s_s[(t_s >= bit_i) & (t_s < bit_i + t_bit / 2)] = ultima_polaridad  # Set the signal for the current bit
            else:
                s_s[(t_s >= bit_i) & (t_s < bit_i + t_bit / 2)] = 0  # Zero voltage for '0'
        
        return t_s, s_s
    
    #decod


    def NRZ_dec(self, t_s, s_s, bit_rate, filter_delay=0):
        t_bit = 1 / bit_rate  # Calculate the duration of a single bit
        if filter_delay > 0:
            s_s = s_s[filter_delay:]
            t_s = t_s[:len(s_s)]
        decoded_bits = []  # List to store the decoded bits
        bit_i_list = []  # List to store bit times (bit_i)
        sample_values_list = []  # List to store actual sample values (s_s[i])
        
        for i in range(len(t_s)):
            bit_i = (i * t_bit / 100)  # Convert index to actual time
            
            # Check if we're at the start of a new bit
            if t_s[i] >= len(decoded_bits) * t_bit:
                # Save the bit time and sample value for tracking
                bit_i_list.append(bit_i)
                sample_values_list.append(s_s[i])
                
                # Detect bit based on the signal level
                if s_s[i] > 0.5:
                    decoded_bits.append(1)
                else:
                    decoded_bits.append(0)
        
        return decoded_bits, np.array(bit_i_list), np.array(sample_values_list)


    def RZ_dec(self, t_s, s_s, bit_rate, filter_delay=0):
        t_bit = 1 / bit_rate  # Calculate the duration of a single bit

        if filter_delay > 0:
            s_s = s_s[filter_delay:]
            t_s = t_s[:len(s_s)]
        
        decoded_bits = []  # List to store the decoded bits
        bit_i_list = []  # List to store bit times (bit_i)
        sample_values_list = []  # List to store actual sample values (s_s[i])
        
        for i in range(len(t_s)):
            bit_i = (i * t_bit / 100)  # Convert index to actual time
            
            # Check if we're at the start of a new bit
            if t_s[i] >= len(decoded_bits) * t_bit:
                # Save the bit time and sample value for tracking
                bit_i_list.append(bit_i)
                sample_values_list.append(s_s[i])
                
                # Detect bit based on the signal level
                if s_s[i] > 0:
                    decoded_bits.append(1)
                elif s_s[i] < 0:
                    decoded_bits.append(0)
                else:
                    decoded_bits.append(0)  # Interpret zero level as '0'
        
        return decoded_bits, np.array(bit_i_list), np.array(sample_values_list)

    def RZ_AMI_dec(self, t_s, s_s, bit_rate, filter_delay=0):
        t_bit = 1 / bit_rate  # Calculate the duration of a single bit
        if filter_delay > 0:
            s_s = s_s[filter_delay:]
            t_s = t_s[:len(s_s)]
    
        decoded_bits = []  # List to store the decoded bits
        bit_i_list = []  # List to store bit times (bit_i)
        sample_values_list = []  # List to store actual sample values (s_s[i])
        
        last_polarity = -1  # Initial state for polarity (-1 for '0', 1 for '1')
        
        for i in range(len(t_s)):
            bit_i = (i * t_bit / 100)  # Convert index to actual time
            
            # Check if we're at the start of a new bit
            if t_s[i] >= len(decoded_bits) * t_bit:
                # Save the bit time and sample value for tracking
                bit_i_list.append(bit_i)
                sample_values_list.append(s_s[i])
                
                # Detect bit based on the threshold
                if s_s[i] > 0:
                    if last_polarity == -1:  # Previous was -1 (no inversion)
                        decoded_bits.append(1)  # A change indicates a '1'
                    else:
                        decoded_bits.append(0)  # No change indicates a '0'
                    last_polarity *= -1  # Invert polarity for the next '1'
                else:
                    decoded_bits.append(0)  # No signal change means '0'
        
        return decoded_bits, np.array(bit_i_list), np.array(sample_values_list)

    def LPF(self, cutoff_freq, rx_sig, order=5):
        nyquist_rate = self.fs / 2.0
        normal_cutoff = cutoff_freq / nyquist_rate
        print(normal_cutoff)
        b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)
        return signal.filtfilt(b, a, rx_sig)

    def awgn(self, snr, signal):
        #Calculate power signal in watts
        signal_watts = signal**2
        sig_power = 10*np.log10(np.mean(signal_watts))

        #Calcular power noise in watts
        noise_db = sig_power - snr
        noise_watts = 10 ** (noise_db / 10)

        mean_noise = 0 

        noise_sig = np.random.normal(mean_noise, np.sqrt(noise_watts), len(signal))

        return signal + noise_sig

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
