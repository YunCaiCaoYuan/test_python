import akshare as ak
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')


class StockDataFetcher:
    """股票数据获取类"""

    def __init__(self):
        self.cache = {}  # 数据缓存

    def get_stock_list(self, market='A股'):
        """获取股票列表"""
        try:
            if market == 'A股':
                # A股列表
                stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
                return stock_zh_a_spot_em_df[['代码', '名称', '最新价', '涨跌幅']]
            elif market == '港股':
                return ak.stock_hk_spot_em()
            elif market == '美股':
                return ak.stock_us_spot_em()
        except Exception as e:
            print(f"获取股票列表失败: {e}")
            return pd.DataFrame()

    def get_daily_data(self, symbol, start_date, end_date, adjust='qfq'):
        """
        获取日线数据

        参数:
            symbol: 股票代码，如 '000001'（平安银行）
            start_date: 开始日期 '2023-01-01'
            end_date: 结束日期 '2023-12-31'
            adjust: 'qfq'前复权, 'hfq'后复权, ''不复权
        """
        cache_key = f"{symbol}_{start_date}_{end_date}_{adjust}"

        if cache_key in self.cache:
            return self.cache[cache_key].copy()

        try:
            # 方法1：使用akshare的通用接口
            stock_zh_a_hist_df = ak.stock_zh_a_hist(
                symbol=symbol,
                period="daily",
                start_date=start_date,
                end_date=end_date,
                adjust=adjust
            )

            if not stock_zh_a_hist_df.empty:
                # 重命名列
                stock_zh_a_hist_df = stock_zh_a_hist_df.rename(columns={
                    '日期': 'date',
                    '开盘': 'open',
                    '收盘': 'close',
                    '最高': 'high',
                    '最低': 'low',
                    '成交量': 'volume',
                    '成交额': 'amount',
                    '振幅': 'amplitude',
                    '涨跌幅': 'pct_chg',
                    '涨跌额': 'change',
                    '换手率': 'turnover'
                })

                # 设置日期索引
                stock_zh_a_hist_df['date'] = pd.to_datetime(stock_zh_a_hist_df['date'])
                stock_zh_a_hist_df.set_index('date', inplace=True)

                # 缓存数据
                self.cache[cache_key] = stock_zh_a_hist_df.copy()

            return stock_zh_a_hist_df

        except Exception as e:
            print(f"获取数据失败 {symbol}: {e}")
            return pd.DataFrame()

    def get_multiple_stocks(self, symbols, start_date, end_date):
        """获取多只股票数据"""
        all_data = {}

        for symbol in symbols:
            print(f"正在获取 {symbol} 数据...")
            data = self.get_daily_data(symbol, start_date, end_date)

            if not data.empty:
                all_data[symbol] = data
            else:
                print(f"警告: {symbol} 数据获取失败")

        return all_data

    def get_index_data(self, symbol='000001', start_date='20230101', end_date='20231231'):
        """获取指数数据"""
        try:
            # 上证指数: 000001, 深证成指: 399001
            index_zh_a_hist_df = ak.index_zh_a_hist(
                symbol=symbol,
                period="daily",
                start_date=start_date,
                end_date=end_date
            )
            return index_zh_a_hist_df
        except Exception as e:
            print(f"获取指数数据失败: {e}")
            return pd.DataFrame()

    def get_realtime_quote(self, symbol):
        """获取实时报价"""
        try:
            stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
            quote = stock_zh_a_spot_em_df[stock_zh_a_spot_em_df['代码'] == symbol]
            return quote
        except:
            return pd.DataFrame()

    def get_financial_data(self, symbol, year='2023'):
        """获取财务数据"""
        try:
            # 资产负债表
            balance_sheet = ak.stock_balance_sheet_em(symbol=symbol, indicator="合并资产负债表")

            # 利润表
            income_statement = ak.stock_profit_sheet_em(symbol=symbol, indicator="合并利润表")

            # 现金流量表
            cash_flow = ak.stock_cash_flow_sheet_em(symbol=symbol, indicator="合并现金流量表")

            return {
                'balance_sheet': balance_sheet,
                'income_statement': income_statement,
                'cash_flow': cash_flow
            }
        except Exception as e:
            print(f"获取财务数据失败: {e}")
            return {}


# 使用示例
if __name__ == "__main__":
    fetcher = StockDataFetcher()

    # 1. 获取股票列表
    stock_list = fetcher.get_stock_list('A股')
    print(f"获取到 {len(stock_list)} 只A股")
    print(stock_list.head())

    # 2. 获取单只股票历史数据
    df = fetcher.get_daily_data('000001', '2023-01-01', '2023-12-31')
    print(f"\n平安银行数据形状: {df.shape}")
    print(df.head())

    # 3. 获取多只股票
    symbols = ['000001', '000002', '600519']  # 平安银行、万科A、贵州茅台
    multi_data = fetcher.get_multiple_stocks(symbols, '2023-01-01', '2023-12-31')

    for symbol, data in multi_data.items():
        print(f"{symbol}: {len(data)} 个交易日")