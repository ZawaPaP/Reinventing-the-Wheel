#include <stdio.h>
#include "data_structures/03_queue/queue_test.h"

int main() {
    fprintf(stderr, "Starting All Tests...\n\n");

    // 各データ構造のテストを実行
    run_queue_tests();
    // 他のテスト実行関数もここで呼び出し

    fprintf(stderr, "\nAll Tests Completed.\n");
    return 0;
}