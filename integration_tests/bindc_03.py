from lpython import (c_p_pointer, CPtr, pointer, i32,
                    Pointer, ccall, p_c_pointer, dataclass,
                    ccallable, empty_c_void_p)

@dataclass
class ArrayWrapped:
    array: CPtr

@ccall(header="bindc_03b.h")
def g(a: CPtr, value: i32, offset_value: bool) -> None:
    pass

def gpy(a: CPtr, value: i32, offset_value: bool) -> None:
    g(a, value, offset_value)

@ccall(header="bindc_03b.h")
def get_array(size: i32) -> CPtr:
    pass

@ccallable
def f(q_void: CPtr) -> None:
    i: i32
    el: i32
    q: Pointer[i32[:]] = c_p_pointer(q_void, i32[:])
    for i in range(10):
        q2: CPtr
        p_c_pointer(pointer(q[i]), q2)
        gpy(q2, i * i, bool(i%2))
        # TODO: Use q[i] directly in the assert.
        el = q[i]
        print(el)
        assert el == i * i + i%2

def h(q_void: CPtr) -> None:
    i: i32
    el: i32
    q: Pointer[i32[:]] = c_p_pointer(q_void, i32[:])
    for i in range(10):
        # TODO: Use q[i] directly in the assert.
        el = q[i]
        print(el)
        assert el == i * i + i%2

def run():
    a: CPtr
    array_wrapped: ArrayWrapped = ArrayWrapped(a)
    array_wrapped1: ArrayWrapped = ArrayWrapped()
    size: i32
    size = 10
    a = get_array(size)
    assert a != empty_c_void_p()
    array_wrapped.array = a
    f(array_wrapped.array)
    array_wrapped1 = array_wrapped
    h(array_wrapped1.array)

run()
