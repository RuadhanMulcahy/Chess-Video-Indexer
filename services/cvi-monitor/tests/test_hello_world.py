from cvi_monitor.operators.hello_world import HelloWorld

def test_hello_world():
    hello_world_operator = HelloWorld()
    assert hello_world_operator.say_hello() == 'Hello World!'