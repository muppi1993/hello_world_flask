import rq_function


def test_add():
    assert rq_function.add(5,4) == 9
    assert rq_function.add(5,10) == 15
    assert rq_function.add(0,0) == 0


def test_count_lines():
    assert rq_function.count_lines('test/testfile1.txt') == 14
    assert rq_function.count_lines('test/testfile2.txt') == 11


def test_poppunk():
    #not really helpful yet, needs improvement, e.g. checking if files got saved?
    assert rq_function.poppunk_assign("/home/mmg220/Documents/flask-tutorial/poppunk") == "/home/mmg220/Documents/flask-tutorial/poppunk/poppunk_clusters_flask"