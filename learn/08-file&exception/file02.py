"""
为了程序健壮性，避免因为以为异常导致程序非法退出
可以使用python自带的异常处理机制
try:
    代码块--可能会发生异常的代码
except <可能会发生的异常> :
    代码块--发生异常时的处理代码
finally:
    代码块--统一操作，无论是否发生异常都会执行

（甚至是调用了sys模块的exit函数退出Python环境，finally块都会被执行，
因为exit函数实质上是引发了SystemExit异常）
"""
def main():
    f = None
    try:
        f = open('致橡树.txt', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()