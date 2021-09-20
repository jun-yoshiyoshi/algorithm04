import math
import heapq
from code06_1 import my_graph


def dijkstra(start, W):
    """
    スタートの頂点と、隣接行列を受け取り、
    到達できる全ての頂点への最短距離を返す。
    """
    # 最短距離の初期値を無限大に設定
    distance_list = [math.inf] * len(W)
    # スタートの頂点だけ、距離を0に設定する
    distance_list[start] = 0
    # 最短距離が確定した頂点
    done_list = []
    # 次に処理する頂点を記録しておくヒープ
    wait_heap = []
    for i, d in enumerate(distance_list):
        # (スタートからの距離、頂点)のタプル
        heapq.heappush(wait_heap, (d, i))

    while wait_heap:
        p = heapq.heappop(wait_heap)
        i = p[1]
        if i in done_list:
            continue
        # スタートからiへの距離を確定する
        done_list.append(i)
        for j, x in enumerate(W[i]):
            if x == 1 and j not in done_list:
                # 緩和
                d = min(distance_list[j], distance_list[i] + x)
                distance_list[j] = d
                # jへの仮の最短距離をdとしてヒープに保存
                heapq.heappush(wait_heap, (d, j))
    return distance_list


print(dijkstra(10, my_graph))
