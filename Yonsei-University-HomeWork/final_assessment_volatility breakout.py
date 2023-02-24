import numpy as np
import matplotlib
import trading_helper
import importlib


importlib.reload(trading_helper)
print(f'Trading Helper Version: {trading_helper.TRADING_HELPER_VERSION}')

AUTH_CODE = '2319d129e17e2cd365363ef4ebfb4596'
trading_helper.set_auth_code(AUTH_CODE)


# 译：[项目1]
#    volatility_breakout() 变动性突破战略函数
#    df - 具有每日价格信息的数据框架
#    k - k 值， 默认值（基本值）为 0.5
#    Qualification 回合中不使用 上升场（bull market？） 分类 (df['cond2'] = 保留为True)
#
def volatility_breakout(df, k=0.1):
    if k < 0:
        return

    # 译：前一天范围 range_s = (High - Low).shift(1)
    df['range_s'] = (df['high'] - df['low']).shift(1)

    # 译：目标买入价=今日开盘价+前一日波幅*k
    df['target'] = df['open'] + df['range_s']*k

    # 如果要使用移动平均线，请按如下方式添加移动平均线列。
    # df['ma5'] = df['close'].rolling(5).mean().shift(1)
    # df['ma20'] = df['close'].rolling(20).mean().shift(1)
    # df['ma50'] = df['close'].rolling(50).mean().shift(1)

    # --------------------------------------------------------------
    # 条件 1 - 波动率突破 ( np.where( High >= Target Bid, True, False ) )
    '''
    Cond1 只接受波动率突破策略的公式。
    '''

    df['cond1'] = np.where(df['high'] >= df['target'], True, False)  # EDIT (3)
    # --------------------------------------------------------------

    # --------------------------------------------------------------
    # 조건 2 - 상승장 구분 (optional)
    # 译：条件 2 - 牛市识别（可选）
    #
    # 在没有任何附加条件的情况下，
    #   df['cond2'] = True
    # 您仅在价格高于 5 日移动平均线时进行交易。
    #   df['cond2'] = np.where( (df['open'] >= df['ma5']), True, False )
    # 如果您只在市场价格高于 3 日移动平均线和 5 日移动平均线时交易
    #   df['cond2'] = np.where( (df['open'] >= df['ma3']) & (df['open'] >= df['ma5']), True, False )
    #
    '''
    cond2 에서 open 이외에 오늘 결정되지 않은 미래의 정보(close, high, low, volume)를 그냥 사용하면 안됩니다.
    译：在cond2中,除了open之外,不能直接使用今天没有决定的未来信息(close, high, low, volume)。
    .shift(1) 를 붙이면 모두 사용 가능합니다.
    译：粘贴了shift(1)即都可使用。

    예를 들어,（ 比如）
    - df['open'] : 사용 가능（可以使用） 
    - df['close'].shift(1) : 사용 가능（可以使用）
    - df['high'] : 사용 불가능（不可以使用）
    - df['low'].shift(1) : 사용 가능（可以使用）
    - df['close'].shift(2) : 사용 가능（可以使用）
    '''
    df['ma5'] = df['close'].rolling(30).mean().shift(1)
    df['ma3'] = df['close'].rolling(3).mean().shift(1)
    df['cond2'] = np.where((df['open'] >= df['ma3']) & (df['open'] >= df['ma5']), True, False)  # EDITABLE
    # df['cond2'] = True
    # --------------------------------------------------------------

    return df


# （获取价格信息）
from_date = '20210401'
to_date = '20221101'
df = trading_helper.get_ohlcv2('KRW-BTC', date1=from_date, date2=to_date )
df.head()


# 函数测试
volatility_breakout(df, 0.5)
hpr, mdd = trading_helper.check_performance_vol(df)
print(f'HPR = {hpr * 100:.1f}%, MDD = {mdd * 100:.1f}%')
volatility_breakout(df, 0.8)
hpr, mdd = trading_helper.check_performance_vol(df)
print(f'HPR = {hpr * 100:.1f}%, MDD = {mdd * 100:.1f}%')

# 期收益率(HPR)变化趋势图）
((df['hpr']-1) * 100).plot(figsize=(15, 3))

# 降幅变化趋势图）
(-df['dd'] * 100).plot(figsize=(15, 3))


# 想要尝试多个k值时）
records = []
for k in np.arange(0.01, 0.9, 0.01):
    volatility_breakout(df, k)
    hpr, mdd = trading_helper.check_performance_vol(df)
    records.append((hpr * 100, mdd * 100, k))

records.sort(reverse=True)

for record in records:
    print(f'HPR= {record[0]:.1f}% MDD= {record[1]:.1f}% k= {record[2]:.2f}')
