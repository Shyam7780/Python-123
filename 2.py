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

    def visit_FunctionDef(self, node):
        self.functions.append(node.name)
        self.function_calls[node.name] = 0
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            if func_name in self.function_calls:
                self.function_calls[func_name] += 1
                self.recursive_calls += 1
        self.generic_visit(node)

    def visit_For(self, node):
        # Ignore constant loops like range(10)
        if isinstance(node.iter, ast.Call) and hasattr(node.iter.func, 'id'):
            if node.iter.func.id == "range":
                if isinstance(node.iter.args[0], ast.Constant):
                    return

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


# ---------------- COMPLEXITY LOGIC ---------------- #
def estimate_complexity(analyzer):
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


# ---------------- GRAPH ---------------- #
def show_graph(complexity):
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
    plt.title(f"{complexity} Growth")
    plt.xlabel("Input Size")
    plt.ylabel("Time")
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

    complexity = estimate_complexity(analyzer)

    result = f"""
Max Loop Depth: {analyzer.max_loop_depth}
Recursive Calls: {analyzer.recursive_calls}
Logarithmic Detected: {analyzer.log_detected}

Estimated Complexity: {complexity}
"""

    result_label.config(text=result)
    show_graph(complexity)


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