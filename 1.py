import tkinter as tk
import ast
import matplotlib.pyplot as plt
import numpy as np

# ---------------- ANALYZER ---------------- #
class ComplexityAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.max_loop_depth = 0
        self.current_depth = 0
        self.functions = []
        self.function_calls = {}
        self.recursive_calls = 0
        self.log_detected = False
        self.current_function = None
        self.list_allocations = 0   # NEW for space complexity

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.function_calls[node.name] = 0
        prev_func = self.current_function
        self.current_function = node.name
        self.generic_visit(node)
        self.current_function = prev_func

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in self.functions:
                self.function_calls[func_name] += 1
                # Proper recursion check
                if func_name == self.current_function:
                    self.recursive_calls += 1
        self.generic_visit(node)

    def visit_For(self, node):
        self.current_depth += 1
        self.max_loop_depth = max(self.max_loop_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_While(self, node):
        # Detect logarithmic behavior (n = n // 2)
        for n in ast.walk(node):
            if isinstance(n, ast.Assign):
                if isinstance(n.value, ast.BinOp):
                    if isinstance(n.value.op, (ast.FloorDiv, ast.Div)):
                        self.log_detected = True
        self.current_depth += 1
        self.max_loop_depth = max(self.max_loop_depth, self.current_depth)
        self.generic_visit(node)
        self.current_depth -= 1

    def visit_ListComp(self, node):
        # Detect list comprehensions (dynamic memory)
        self.list_allocations += 1
        self.generic_visit(node)

    def visit_List(self, node):
        # Detect explicit list creation
        self.list_allocations += 1
        self.generic_visit(node)


# ---------------- COMPLEXITY LOGIC ---------------- #
def estimate_time_complexity(analyzer):
    depth = analyzer.max_loop_depth

    # Recursion cases
    if analyzer.recursive_calls > 1:
        return "O(2^n) (Exponential Recursion)"
    elif analyzer.recursive_calls == 1:
        return "O(n) (Linear Recursion)"

    # Logarithmic detection
    if analyzer.log_detected:
        return "O(log n)"

    # Loop-based complexity
    if depth == 0:
        return "O(1)"
    elif depth == 1:
        return "O(n)"
    else:
        return f"O(n^{depth})"


def estimate_space_complexity(analyzer):
    if analyzer.recursive_calls > 0 and analyzer.list_allocations > 0:
        return "O(n) (Recursion stack + dynamic array)"
    elif analyzer.recursive_calls > 0:
        return "O(n) (Recursion stack)"
    elif analyzer.list_allocations > 1:
        return "O(n) (Multiple dynamic arrays)"
    elif analyzer.list_allocations == 1:
        return "O(n) (Single dynamic array)"
    else:
        return "O(1)"


# ---------------- GRAPH ---------------- #
def show_graph(complexity, label="Time Complexity"):
    n = np.arange(1, 50)

    if "log" in complexity:
        y = np.log(n)
    elif "2^n" in complexity:
        y = 2**n
    elif "n^2" in complexity:
        y = n**2
    elif "n^3" in complexity:
        y = n**3
    elif "n" in complexity:
        y = n
    else:
        y = np.ones_like(n)

    plt.plot(n, y)
    plt.title(f"{complexity} Growth ({label})")
    plt.xlabel("Input Size")
    plt.ylabel("Usage")
    plt.show()


# ---------------- MAIN ---------------- #
def analyze_code():
    code = text_box.get("1.0", tk.END)

    try:
        tree = ast.parse(code)
    except:
        result_label.config(text="Syntax Error in Code")
        return

    analyzer = ComplexityAnalyzer()
    analyzer.visit(tree)

    time_complexity = estimate_time_complexity(analyzer)
    space_complexity = estimate_space_complexity(analyzer)

    result = f"""
Max Loop Depth: {analyzer.max_loop_depth}
Recursive Calls: {analyzer.recursive_calls}
Logarithmic Detected: {analyzer.log_detected}
List Allocations: {analyzer.list_allocations}

Estimated Time Complexity: {time_complexity}
Estimated Space Complexity: {space_complexity}
"""

    result_label.config(text=result)
    show_graph(time_complexity, "Time Complexity")
    show_graph(space_complexity, "Space Complexity")


def auto_analyze(event=None):
    root.after(500, analyze_code)


# ---------------- GUI ---------------- #
root = tk.Tk()
root.title("Advanced Code Complexity Analyzer")
root.geometry("800x600")

title = tk.Label(root, text="Advanced AI Code Complexity Analyzer", font=("Arial", 16))
title.pack()

text_box = tk.Text(root, height=20, width=90)
text_box.pack()

text_box.bind("<KeyRelease>", auto_analyze)

analyze_btn = tk.Button(root, text="Analyze Code", command=analyze_code)
analyze_btn.pack(pady=10)

result_label = tk.Label(root, text="", justify="left")
result_label.pack()

root.mainloop()