#include <string>
#include <vector>
#include <cmath>
#include <sstream>

using namespace std;

// 소수 판별 함수
bool isPrime(long long num) {
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;
    for (long long i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) return false;
    }
    return true;
}

// n을 k진수로 변환하는 함수
string toKBase(int n, int k) {
    string result = "";
    while (n > 0) {
        result = to_string(n % k) + result;
        n /= k;
    }
    return result;
}

int solution(int n, int k) {
    // 1. n을 k진수로 변환
    string kBaseNumber = toKBase(n, k);

    // 2. 조건에 맞는 소수 찾기
    stringstream ss(kBaseNumber);
    string segment;
    int answer = 0;
    
    while (getline(ss, segment, '0')) {
        if (!segment.empty()) {
            long long num = stoll(segment);
            if (isPrime(num)) {
                answer++;
            }
        }
    }

    return answer;
}