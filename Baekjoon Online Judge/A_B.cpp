#include <iostream>

int sum(int A, int B) {
    return A + B;
}

int main() {
    int A, B;
    std::cin >> A >> B;
    std::cout << sum(A, B) << std::endl;
    return 0;
}
