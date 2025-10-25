
import download_stock
import fourier_func
import plot_func


stock_input = input('ENTER stock TICKER and press ENTER >> ')
stock = stock_input.upper()

df = download_stock.download(stock)
#print(df)


#Apply custom Kalman filter
df_fft = fourier_func.func_furier_new_series( df, stock, frequency_threshold = 0.1, plot = True )

#print(df_fft)

plot_func.ploter(df_fft, stock, 'filtered__fft')
