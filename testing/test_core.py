from kahn.core import ForwardingEngine


def test_forward(mock_serial):
    stub = mock_serial.stub(
        name="foo",
        receive_bytes=b"__start__",
        send_bytes=b"$IIVWR,154.0,L,11.06,N,5.69,M,20.48,K*65",
    )
    forwarder = ForwardingEngine(source=f"serial://{mock_serial.port}", target="file:///dev/stdout")
    forwarder.reader.write(b"__start__")
    message = forwarder.process()
    assert message == b"$IIVWR,154.0,L,11.06,N,5.69,M,20.48,K*65"

    # TODO: Implement and verify output being received on STDOUT.
