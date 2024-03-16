import util

class PageRank:
    def __init__(self, iterations=100, damping_factor=0.85):
        self.iterations = iterations
        self.damping_factor = damping_factor

    ### Version One ###
    def calc_pagerank(self, graph):
        # Step 1: Initialization - Initialize each page's rank equally among all nodes in the graph
        page_rank = {node: 1/len(graph) for node in graph}

        # Step 2: Iteration Loop - Repeat the process a predetermined number of times (self.iterations)
        for _ in range(self.iterations):
            new_ranks = {}

            # Step 3: Rank Calculation - Calculate the new rank for each node based on incoming links
            for node in graph:
                new_rank = 0
                # Step 4: Accumulate Rank from Neighbors - Sum the ranks of all neighbors pointing to this node, adjusted for their number of outbound links
                for neighbor in graph:
                    if node in graph[neighbor]:  # If the node is a neighbor
                        new_rank += page_rank[neighbor] / len(graph[neighbor])
                new_ranks[node] = new_rank

            # Step 5: Update PageRank Scores - Update the ranks for all nodes based on this iteration's calculations
            page_rank = new_ranks

        # Return the final PageRank scores after completing all iterations
        return page_rank

    ### Version Two (Damping) ###
    def calc_pagerank_with_damping(self, graph):
        # Step 1: Initialization - Initialize each page's rank equally among all nodes in the graph
        page_rank = {node: 1/len(graph) for node in graph}

        # Step 2: Iteration Loop - Repeat the process a predetermined number of times (self.iterations)
        for _ in range(self.iterations):
            new_ranks = {}

            # Step 3: Rank Calculation - Calculate the new rank for each node based on incoming links and the damping factor
            for node in graph:
                new_rank = 0
                # Step 4: Accumulate Rank from Neighbors - Sum the ranks of all neighbors pointing to this node, adjusted for their number of outbound links
                for neighbor in graph:
                    if node in graph[neighbor]:  # If the node is a neighbor
                        new_rank += page_rank[neighbor] / len(graph[neighbor])
                # Apply the damping factor to the calculated rank
                new_ranks[node] = (1 - self.damping_factor) / len(graph) + self.damping_factor * new_rank

            # Step 5: Update PageRank Scores - Update the ranks for all nodes based on this iteration's calculations
            page_rank = new_ranks

        # Return the final PageRank scores after completing all iterations
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

# Basic PageRank scores
page_rank_scores = pr.calc_pagerank(graph)
site_scores = util.toString(page_rank_scores)
print("Basic PageRank scores:", site_scores)

# PageRank scores with damping
page_rank_scores_with_damping = pr.calc_pagerank_with_damping(graph)
site_scores_with_damping = util.toString(page_rank_scores_with_damping)
print("PageRank scores with damping:", site_scores_with_damping)

'''
Output:
Basic PageRank scores: {'Website A': 0.2, 'Website B': 0.30000000000000004, 'Website C': 0.2, 'Website D': 0.30000000000000004, 'Website E': 0}
PageRank scores with damping: {'Website A': 0.23690036520596677, 'Website B': 0.2480996347940332, 'Website C': 0.23690036520596677, 'Website D': 0.2480996347940332, 'Website E': 0.030000000000000006}
'''