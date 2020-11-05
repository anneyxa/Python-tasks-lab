from graph import Graph
from textgenerator import TextParser

if __name__ == '__main__':
    # simple tests for graph class

    # g = Graph()
    # g.add_vertex("a")
    # g.add_vertex("b")
    # g.add_vertex("c")
    # print(g.get_vertices())
    # g.delete_vertex("a")
    # print(g.get_vertices())
    # g.add_edge({"b", "c"})
    # print(g.get_edges())
    #
    # g2 = Graph({"a": ["b", "c"],
    #          "b": ["a", "d"],
    #          "c": ["a", "d"],
    #          "d": ["e"],
    #          })
    # print(g2.get_vertices())
    # print(g2.get_edges())
    # g2.add_vertex("f")
    # g2.add_edge({"g", "h"})
    # print(g2.get_vertices())
    # print(g2.get_edges())
    # print(g2.get_all_neighbours_of_vertex("b"))
    #
    # print(g2.dfs("a"))
    # print(g2.bfs("a"))
    #______________________________________________

    # tests for textgenerator class

    path_txt = "nkjp.txt"
    path_conll = "nkjp.conll"

    # for token in TextParser.get_tokens_txt(path_txt):
    #     print(token)
    #
    # for token in TextParser.get_tokens_conll(path_conll):
    #     print(token)
    #
    # for sent in TextParser.get_sentences_txt(path_txt):
    #     print(sent)
    #
    # for sent in TextParser.get_sentences_conll(path_conll):
    #     print(sent)
