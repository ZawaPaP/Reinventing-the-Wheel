#include "queue.h"
#include <stdio.h>

int main() {
    Queue* q = init();
    if (q == NULL) {
        fprintf(stderr, "Failed to initialize queue\n");
        return 1;
    }

    // デモコード
    Position p1 = {1, 2};
    Position p2 = {3, 4};
    
    push(q, p1);
    push(q, p2);
    
    Position popped = pop(q);
    printf("Popped: (%d, %d)\n", popped.x, popped.y);

    freeQueue(q);
    return 0;
}