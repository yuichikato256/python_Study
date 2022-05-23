def get_stooq( code ) :
  import pandas as pd
  df = pd.read_csv( f'https://stooq.com/q/d/l/?s={ code }&i=d' ,index_col=0 )
  df.index = pd.to_datetime( df.index ).tz_localize( 'Asia/Tokyo' )
  return df


print(get_stooq( '7203.jp' ))
 