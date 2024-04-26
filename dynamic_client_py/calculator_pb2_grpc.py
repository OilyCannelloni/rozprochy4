# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import calculator_pb2 as calculator__pb2


class CalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddTwo = channel.unary_unary(
                '/calculator.Calculator/AddTwo',
                request_serializer=calculator__pb2.ArithmeticOpArguments.SerializeToString,
                response_deserializer=calculator__pb2.SingleIntResult.FromString,
                )
        self.SubtractTwo = channel.unary_unary(
                '/calculator.Calculator/SubtractTwo',
                request_serializer=calculator__pb2.ArithmeticOpArguments.SerializeToString,
                response_deserializer=calculator__pb2.SingleIntResult.FromString,
                )


class CalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubtractTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddTwo': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTwo,
                    request_deserializer=calculator__pb2.ArithmeticOpArguments.FromString,
                    response_serializer=calculator__pb2.SingleIntResult.SerializeToString,
            ),
            'SubtractTwo': grpc.unary_unary_rpc_method_handler(
                    servicer.SubtractTwo,
                    request_deserializer=calculator__pb2.ArithmeticOpArguments.FromString,
                    response_serializer=calculator__pb2.SingleIntResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculator.Calculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Calculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/AddTwo',
            calculator__pb2.ArithmeticOpArguments.SerializeToString,
            calculator__pb2.SingleIntResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SubtractTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.Calculator/SubtractTwo',
            calculator__pb2.ArithmeticOpArguments.SerializeToString,
            calculator__pb2.SingleIntResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class AdvancedCalculatorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.MultiplyTwo = channel.unary_unary(
                '/calculator.AdvancedCalculator/MultiplyTwo',
                request_serializer=calculator__pb2.ArithmeticOpArguments.SerializeToString,
                response_deserializer=calculator__pb2.SingleIntResult.FromString,
                )
        self.ListSumComplex = channel.unary_unary(
                '/calculator.AdvancedCalculator/ListSumComplex',
                request_serializer=calculator__pb2.ListComplexOpArguments.SerializeToString,
                response_deserializer=calculator__pb2.Complex.FromString,
                )
        self.ListSum = channel.unary_unary(
                '/calculator.AdvancedCalculator/ListSum',
                request_serializer=calculator__pb2.ListArithmeticOpArguments.SerializeToString,
                response_deserializer=calculator__pb2.SingleIntResult.FromString,
                )


class AdvancedCalculatorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def MultiplyTwo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSumComplex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSum(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AdvancedCalculatorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'MultiplyTwo': grpc.unary_unary_rpc_method_handler(
                    servicer.MultiplyTwo,
                    request_deserializer=calculator__pb2.ArithmeticOpArguments.FromString,
                    response_serializer=calculator__pb2.SingleIntResult.SerializeToString,
            ),
            'ListSumComplex': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSumComplex,
                    request_deserializer=calculator__pb2.ListComplexOpArguments.FromString,
                    response_serializer=calculator__pb2.Complex.SerializeToString,
            ),
            'ListSum': grpc.unary_unary_rpc_method_handler(
                    servicer.ListSum,
                    request_deserializer=calculator__pb2.ListArithmeticOpArguments.FromString,
                    response_serializer=calculator__pb2.SingleIntResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'calculator.AdvancedCalculator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AdvancedCalculator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def MultiplyTwo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.AdvancedCalculator/MultiplyTwo',
            calculator__pb2.ArithmeticOpArguments.SerializeToString,
            calculator__pb2.SingleIntResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSumComplex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.AdvancedCalculator/ListSumComplex',
            calculator__pb2.ListComplexOpArguments.SerializeToString,
            calculator__pb2.Complex.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListSum(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/calculator.AdvancedCalculator/ListSum',
            calculator__pb2.ListArithmeticOpArguments.SerializeToString,
            calculator__pb2.SingleIntResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
