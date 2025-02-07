
def compare_t_shirt(a, b):
        
        if a == b:
            return "="
        if a[-1] == 'M':
            return ">" if b[-1] != 'M' else "<"
        if b[-1] == 'M':
            return "<" if a[-1] != 'M' else ">"
        if a[-1] == 'S':
            if b[-1] == 'L':
                return "<"
            return "<" if len(a) > len(b) else ">"
        if a[-1] == 'L':
            if b[-1] == 'S':
                return ">"
            return ">" if len(a) > len(b) else "<"
    
# def compare_t_shirts(a,b):
#     if a == b:
#         return "="
#     if a[-1] == "M":
#         return 

t = int(input())
for _ in range(t):
    a, b = input().split()
    print(compare_t_shirt(a, b))