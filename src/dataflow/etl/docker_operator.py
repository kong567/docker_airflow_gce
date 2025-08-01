from datetime import datetime
# 從 Airflow 匯入 DockerOperator，用來在 DAG 中執行 Docker 容器任務
from airflow.operators.docker_operator import (
    DockerOperator,
)





# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def crawler_cnyes_headlines(month) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"crawler_cnyes_headlines_{month}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/crawler_cnyes_headlines.py {month}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="crawler_cnyes_headlines",
    )


def crawler_cnyes_headlines_daily(today) -> DockerOperator:
    dt = datetime.today()
    day = dt.strftime('%Y%m%d')
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"crawler_cnyes_headlines_daily_{day}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/crawler_cnyes_headlines_daily.py {today}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="crawler_cnyes_headlines",
    )



# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def ETF_historyprice(tickers) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"ETF_historyprice_{tickers}",
        image="qweasdkimo123/crawler:0.0.4",
        command = f"pipenv run python crawler/ETF_historyprice.py {tickers}",
        # command=f"pipenv run python crawler/ETF_historyprice.py {tickers}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="ETF_historyprice",
    )





# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def ETF_PremiumDiscount(tickers) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"ETF_PremiumDiscount_{tickers}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/ETF_PremiumDiscount.py {tickers}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="ETF_PremiumDiscount",
    )




# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def MagaBank_NEWS(news_date) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"MagaBank_NEWS_{news_date}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/MagaBank_NEWS.py {news_date}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="MagaBank_NEWS",
    )

# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def MagaBank_NEWS_daily(news_date) -> DockerOperator:
    dt = datetime.today()
    day = dt.strftime('%Y%m%d')
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"MagaBank_NEWS_daily_{day}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/MagaBank_NEWS_daily.py {news_date}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="MagaBank_NEWS",
    )



# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def ptt(start_index) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"ptt{start_index}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/ptt.py {start_index}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="ptt",
    )



# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def ptt_daily(target_today) -> DockerOperator:
    dt = datetime.today()
    day = dt.strftime('%Y%m%d')
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"ptt_daily_{day}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/ptt_daily.py {target_today}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="ptt",
    )




# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def vix(Volatility_Index) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id="vix",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/vix.py {Volatility_Index}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
        # queue="vix",
    )


# 建立一個 DockerOperator 任務的函式，回傳一個 Airflow 的任務實例
def sentiment(STOCK_ID) -> DockerOperator:
    return DockerOperator(
        # 設定這個 task 在 DAG 中的名稱（唯一識別碼）
        task_id=f"ETF_singal_{STOCK_ID}",
        image="qweasdkimo123/crawler:0.0.4",
        command=f"pipenv run python crawler/ETF_signal.py {STOCK_ID}",
        # 每次執行前都強制重新拉取最新的 image（確保使用最新版本）
        force_pull=True,
        # 容器執行完畢後自動刪除（避免堆積殘留容器）
        auto_remove=True,
        # ✅ 指定容器要使用的 Docker network 名稱
        # 注意：這要是 Docker Engine 中已存在的 network 名稱
        network_mode="my_swarm_network",
        queue = "All_crawler",
    )
