import os

# ❌ Insecure: Using eval (Bandit should flag this)
def run_code(user_input: str):
    return eval(user_input)

def add(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    print("Demo App Running...")
    print("2 + 3 =", add(2, 3))
    # Intentional insecure call
    user_code = "2+2"
    print("Eval result:", run_code(user_code))
#test0013
