#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <filesystem>

std::string readFileContents(const std::string& filePath) {
    std::ifstream file(filePath);
    if (!file.is_open()) {
        throw std::runtime_error("Could not open file: " + filePath);
    }
    std::string contents((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
    return contents;
}

std::map<std::string, std::string> readAllFilesInDirectory(const std::string& directoryPath) {
    std::map<std::string, std::string> fileContents;
    for (const auto& entry : std::filesystem::directory_iterator(directoryPath)) {
        if (entry.is_regular_file()) {
            std::string filePath = entry.path().string();
            std::string fileName = entry.path().filename().string();
            fileContents[fileName] = readFileContents(filePath);
        }
    }
    return fileContents;
}