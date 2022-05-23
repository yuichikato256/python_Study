def calc_techs( df ) :
  import talib as ta
  import numpy as np
  df['Highest20'] = np.append( np.nan ,ta.MAX( df['High'].values ,20 )[:-1] )
  df['Highest10'] = np.append( np.nan ,ta.MAX( df['High'].values ,10 )[:-1] )
  df['Lowest20'] = np.append( np.nan ,ta.MIN( df['Low'].values ,20 )[:-1] )
  df['Lowest10'] = np.append( np.nan ,ta.MIN( df['Low'].values ,10 )[:-1] )
  df['EMA350'] = ta.EMA( df['Close'].values ,350 )
  df['EMA25'] = ta.EMA( df['Close'].values ,25 )
  df['ATR20'] = ta.ATR( df['High'].values ,df['Low'].values ,df['Close'].values ,20 )
  return df

def get_stooq( code ) :
  import pandas as pd
  df = pd.read_csv( f'https://stooq.com/q/d/l/?s={ code }&i=d' ,index_col=0 )
  df.index = pd.to_datetime( df.index ).tz_localize( 'Asia/Tokyo' )
  return df

df = get_stooq('7203.jp')
calc_techs( df ) 
print(df)


