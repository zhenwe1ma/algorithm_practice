#include <iostream>
#include <limits>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using Graph = std::unordered_map<std::string, std::vector<std::pair<std::string, int>>>;

std::unordered_map<std::string, long long> Dijkstra(const Graph& graph,
                                                   const std::string& start) {
    std::set<std::string> nodes;
    for (const auto& [node, neighbors] : graph) {
        nodes.insert(node);
        for (const auto& [neighbor, weight] : neighbors) {
            nodes.insert(neighbor);
        }
    }
    nodes.insert(start);

    const long long kInf = std::numeric_limits<long long>::max() / 4;
    std::unordered_map<std::string, long long> distances;
    for (const auto& node : nodes) {
        distances[node] = kInf;
    }
    distances[start] = 0;

    std::unordered_set<std::string> visited;
    while (visited.size() < nodes.size()) {
        std::string current;
        long long current_distance = kInf;

        for (const auto& node : nodes) {
            if (!visited.count(node) && distances[node] < current_distance) {
                current = node;
                current_distance = distances[node];
            }
        }

        if (current.empty()) {
            break;
        }

        visited.insert(current);
        auto it = graph.find(current);
        if (it == graph.end()) {
            continue;
        }

        for (const auto& [neighbor, weight] : it->second) {
            const long long new_distance = distances[current] + weight;
            if (new_distance < distances[neighbor]) {
                distances[neighbor] = new_distance;
            }
        }
    }

    return distances;
}

int main() {
    Graph graph = {
        {"A", {{"B", 5}, {"C", 2}}},
        {"B", {{"D", 4}}},
        {"C", {{"B", 1}, {"D", 7}}},
        {"D", {}},
    };

    const std::string start = "A";
    const auto distances = Dijkstra(graph, start);
    const long long kInf = std::numeric_limits<long long>::max() / 4;

    std::set<std::string> nodes;
    for (const auto& [node, _] : distances) {
        nodes.insert(node);
    }

    for (const auto& node : nodes) {
        std::cout << start << " -> " << node << ": ";
        if (distances.at(node) == kInf) {
            std::cout << "inf";
        } else {
            std::cout << distances.at(node);
        }
        std::cout << '\n';
    }

    return 0;
}
