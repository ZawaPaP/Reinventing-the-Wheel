CC := gcc
CFLAGS := -Wall -Wextra -Werror

# ディレクトリ設定
SRC_DIR := src
TEST_DIR := tests
BUILD_DIR := build

# ソースファイル
MAIN_SRCS := $(shell find $(SRC_DIR) -name 'main.c')
# ディレクトリごとのルートパスを取得（main.c があるディレクトリ）
MAIN_DIRS := $(sort $(dir $(MAIN_SRCS)))

# 実行ファイル名に変換（build/data_structures/03_queue など）
EXES := $(patsubst $(SRC_DIR)/%/main.c, $(BUILD_DIR)/%, $(MAIN_SRCS))

# テストファイル
TEST_SRCS := $(shell find $(TEST_DIR) -name '*.c')
TEST_TARGET := $(BUILD_DIR)/test

# すべてのソースファイル（main.cを除く）
OTHER_SRCS := $(filter-out $(MAIN_SRCS), $(shell find $(SRC_DIR) -name '*.c'))

# デフォルトターゲット（ソースファイルのビルド）
all: $(EXES)

# テストのビルドと実行
test: $(TEST_TARGET)
	./$(TEST_TARGET)

# 各実行ファイルを作成
$(BUILD_DIR)/%: $(SRC_DIR)/%/main.c $(SRC_DIR)/%/*.c | $(BUILD_DIR)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(SRC_DIR)/$*/main.c $(filter-out $(SRC_DIR)/$*/main.c, $(wildcard $(SRC_DIR)/$*/*.c)) -o $@

# テスト実行ファイルのビルド
$(TEST_TARGET): $(TEST_SRCS) $(OTHER_SRCS) | $(BUILD_DIR)
	@mkdir -p $(@D)
	$(CC) $(CFLAGS) $(OTHER_SRCS) $(TEST_SRCS) -o $@

# ディレクトリ作成
$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all clean test
