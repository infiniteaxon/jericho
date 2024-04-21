#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <thread>
#include <mutex>
#include <future>

std::map<char, std::vector<std::string>> substitutions = {
    {'a', {"A", "a", "4", "@"}},
    {'b', {"B", "b", "8"}},
    {'c', {"C", "c", "<", "("}},
    {'d', {"D", "d", "|)"}},
    {'e', {"E", "e", "3", "&"}},
    {'f', {"f", "F"}},
    {'g', {"G", "g", "6"}},
    {'h', {"H", "h", "#"}},
    {'i', {"I", "i", "1", "!", "|"}},
    {'j', {"J", "j"}},
    {'k', {"K", "k", "|<"}},
    {'l', {"L", "l", "1", "|"}},
    {'m', {"M", "m"}},
    {'n', {"N", "n"}},
    {'o', {"O", "o", "0", "()"}},
    {'p', {"P", "p"}},
    {'q', {"Q", "q", "9"}},
    {'r', {"R", "r"}},
    {'s', {"S", "s", "5", "$"}},
    {'t', {"T", "t", "7", "+"}},
    {'u', {"U", "u", "|_|", "(_)"}},
    {'v', {"V", "v"}},
    {'w', {"W", "w"}},
    {'x', {"X", "x", "><"}},
    {'y', {"Y", "y"}},
    {'z', {"Z", "z", "2"}}
};

std::vector<std::string> number_patterns = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"};
std::vector<std::string> special_chars = {"!", "@", "#", "$", "%", "^", "&", "*", "-", "_", "+"};

// Generate all possible combinations from a password
std::set<std::string> generate_combinations(const std::string& pwd) {
    std::set<std::string> results;
    std::vector<std::vector<std::string>> options;
    for (char c : pwd) {
        if (substitutions.count(c)) {
            options.push_back(substitutions[c]);
        } else {
            options.push_back({std::string(1, c)});
        }
    }
    
    std::function<void(size_t, std::string)> combine = [&](size_t index, std::string accum) {
        if (index == options.size()) {
            results.insert(accum);
            return;
        }
        for (const auto& s : options[index]) {
            combine(index + 1, accum + s);
        }
    };

    combine(0, "");
    return results;
}

// Pattern generation for different levels
std::set<std::string> level_2_patterns(const std::string& v) {
    std::set<std::string> results;
    std::vector<std::string> all_options = number_patterns;
    all_options.insert(all_options.end(), special_chars.begin(), special_chars.end());
    for (const auto& s : all_options) {
        for (const auto& t : all_options) {
            results.insert(v + s + t);
            results.insert(s + v + t);
            results.insert(s + t + v);
        }
    }
    return results;
}

std::set<std::string> level_3_patterns(const std::string& v) {
    std::set<std::string> results;
    std::vector<std::string> all_options = number_patterns;
    all_options.insert(all_options.end(), special_chars.begin(), special_chars.end());
    for (const auto& s : all_options) {
        for (const auto& t : all_options) {
            for (const auto& u : all_options) {
                results.insert(v + s + t + u);
                results.insert(s + v + t + u);
                results.insert(s + t + v + u);
                results.insert(s + t + u + v);
            }
        }
    }
    return results;
}

std::set<std::string> level_4_patterns(const std::string& v) {
    std::set<std::string> results;
    std::vector<std::string> all_options = number_patterns;
    all_options.insert(all_options.end(), special_chars.begin(), special_chars.end());
    for (const auto& s : all_options) {
        for (const auto& t : all_options) {
            for (const auto& u : all_options) {
                for (const auto& w : all_options) {
                    results.insert(v + s + t + u + w);
                    results.insert(s + v + t + u + w);
                    results.insert(s + t + v + u + w);
                    results.insert(s + t + u + v + w);
                    results.insert(s + t + u + w + v);
                }
            }
        }
    }
    return results;
}

// Main function that demonstrates pattern generation
int main(int argc, char* argv[]) {
    if (argc < 3) {
        std::cerr << "Usage: " << argv[0] << " <password> <level>\n";
        return 1;
    }

    std::string password = argv[1];
    int level = std::stoi(argv[2]);

    std::set<std::string> final_variants = generate_combinations(password);
    std::set<std::string> new_variants;

    if (level >= 2) {
        for (const auto& base : final_variants) {
            auto variants = level_2_patterns(base);
            new_variants.insert(variants.begin(), variants.end());
        }
        final_variants.insert(new_variants.begin(), new_variants.end());
    }
    if (level >= 3) {
        new_variants.clear();
        for (const auto& base : final_variants) {
            auto variants = level_3_patterns(base);
            new_variants.insert(variants.begin(), variants.end());
        }
        final_variants.insert(new_variants.begin(), new_variants.end());
    }
    if (level >= 4) {
        new_variants.clear();
        for (const auto& base : final_variants) {
            auto variants = level_4_patterns(base);
            new_variants.insert(variants.begin(), variants.end());
        }
        final_variants.insert(new_variants.begin(), new_variants.end());
    }

    // Open an ofstream to write output to a file
    std::ofstream outfile("output.txt");
    if (!outfile.is_open()) {
        std::cerr << "Failed to open output file." << std::endl;
        return 1;
    }

    // Output all generated variants to the file
    for (const auto& variant : final_variants) {
        outfile << variant << std::endl;
    }

    // Close the output file
    outfile.close();

    return 0;
}
