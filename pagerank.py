import util
class PageRank:
    def __init__(self, iterations=100, damping_factor=0.85):
        self.iterations = iterations
        self.damping_factor = damping_factor

    def calc_pagerank(self, graph):
 
        return page_rank

    def calc_pagerank_with_damping(self, graph, damping_factor=0.85):
    
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
