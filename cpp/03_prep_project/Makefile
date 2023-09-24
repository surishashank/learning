# Compiler
CXX := g++
# Compiler flags
CXXFLAGS := -std=c++17
# Name of the executable
TARGET := get_order_book
# Directory containing source files
SRCDIR := .
# Directory for object files
BUILDDIR := build

SOURCES := $(filter-out $(SRCDIR), $(wildcard $(SRCDIR)/*.cpp))
OBJECTS := $(patsubst $(SRCDIR)/%.cpp,$(BUILDDIR)/%.o,$(SOURCES))
LIBS := -lcurl

# $(info OBJECTS: $(OBJECTS))

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) $^ -o $@ $(LIBS)

$(BUILDDIR)/%.o: $(SRCDIR)/%.cpp
	@mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -rf $(BUILDDIR) $(TARGET)
