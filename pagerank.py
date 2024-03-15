import util

class PageRank:
    def __init__(self, iterations=100, damping_factor=0.85):
        self.iterations = iterations
        self.damping_factor = damping_factor

    def calc_pagerank(self, graph):
        page_rank = {node: 1/len(graph) for node in graph}  # Initialize each page's rank
        for _ in range(self.iterations):
            new_ranks = {}
            for node in graph:
                new_rank = sum((page_rank[neighbor] / len(graph[neighbor]) for neighbor in graph if node in graph[neighbor]), 0)
                new_ranks[node] = (1 - self.damping_factor) / len(graph) + self.damping_factor * new_rank
            page_rank = new_ranks
        return page_rank

    def calc_pagerank_with_damping(self, graph):
        page_rank = {node: 1/len(graph) for node in graph}  # Initialize each page's rank
        for _ in range(self.iterations):
            new_ranks = {}
            for node in graph:
                new_rank = sum((page_rank[neighbor] / len(graph[neighbor]) for neighbor in graph if node in graph[neighbor]), 0)
                new_ranks[node] = (1 - self.damping_factor) / len(graph) + self.damping_factor * new_rank
            page_rank = new_ranks
        return page_rank

graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['D'],
    'D': ['A'],
    'E': ['C', 'A']
}

pr = PageRank(iterations=10)
util.draw_graph(graph)

page_rank_scores = pr.calc_pagerank(graph)
site_scores = util.toString(page_rank_scores)
print(site_scores)

page_rank_scores = pr.calc_pagerank_with_damping(graph)
site_scores = util.toString(page_rank_scores)
print(site_scores)
