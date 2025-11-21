class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        ##Dijkstra's
        # graph: list[list[int]] = [[] for _ in range(n)]
        # for node1,node2,distance in edges:
        #     graph[node1].append([node2,distance])
        #     graph[node2].append([node1,distance])
        
        # def get_num_of_neighbors_in_distance(source:int)->int:
        #     queue: list[tuple[int,int]]=[(0,source)]
        #     visited=set()

        #     while queue:
        #         distance_to_this_node, cur_node= heappop(queue)
        #         if not cur_node in visited:
        #             visited.add(cur_node)
        #             for neighbor, distance in graph[cur_node]:
        #                 distance_from_source = distance_to_this_node + distance
        #                 if distance_from_source<=distanceThreshold:
        #                     heappush(queue, (distance_from_source, neighbor))
        #     return len(visited)-1
        
        # minimum_number:int = n
        # res: int = None

        # for source in range(n):
        #     neighbors:int = get_num_of_neighbors_in_distance(source)
        #     if neighbors<=minimum_number:
        #         minimum_number=neighbors
        #         res=source
        # return res

        #Floyd-Warshall
        distance = [[float('inf') for _ in range(n)] for _ in range(n)]
        for node in range(n):
            distance[node][node] = 0
        
        for node1, node2, dist in edges:
            distance[node1][node2]=dist
            distance[node2][node1]=dist
        
        for middle in range(n):
            for source in range(n):
                for destination in range(n):
                    distance[source][destination]=min(distance[source][destination], distance[source][middle]+distance[middle][destination])
        min_num = n
        res = None

        for source in range(n):
            source_count=0
            for destination in range(n):
                if distance[source][destination]<=distanceThreshold:
                    source_count+=1
            if source_count<=min_num:
                min_num=source_count
                res=source
        return res
