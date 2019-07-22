#
# Autogenerated by Thrift Compiler (0.12.1)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:slots
#
import logging
import sys

from thrift.protocol.TProtocol import TProtocolException
from thrift.Thrift import TApplicationException
from thrift.Thrift import TException
from thrift.Thrift import TFrozenDict
from thrift.Thrift import TMessageType
from thrift.Thrift import TProcessor
from thrift.Thrift import TType
from thrift.transport import TTransport
from thrift.TRecursive import fix_spec

from .ttypes import *

all_structs = []


class Iface(object):
    def example(self):
        pass


class Client(Iface):
    def __init__(self, iprot, oprot=None):
        self._iprot = self._oprot = iprot
        if oprot is not None:
            self._oprot = oprot
        self._seqid = 0

    def example(self):
        self.send_example()
        return self.recv_example()

    def send_example(self):
        self._oprot.writeMessageBegin("example", TMessageType.CALL, self._seqid)
        args = example_args()
        args.write(self._oprot)
        self._oprot.writeMessageEnd()
        self._oprot.trans.flush()

    def recv_example(self):
        iprot = self._iprot
        (fname, mtype, rseqid) = iprot.readMessageBegin()
        if mtype == TMessageType.EXCEPTION:
            x = TApplicationException()
            x.read(iprot)
            iprot.readMessageEnd()
            raise x
        result = example_result()
        result.read(iprot)
        iprot.readMessageEnd()
        if result.success is not None:
            return result.success
        if result.exc is not None:
            raise result.exc
        raise TApplicationException(
            TApplicationException.MISSING_RESULT, "example failed: unknown result"
        )


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["example"] = Processor.process_example

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(
                TApplicationException.UNKNOWN_METHOD, "Unknown function %s" % (name)
            )
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            self._processMap[name](self, seqid, iprot, oprot)
        return True

    def process_example(self, seqid, iprot, oprot):
        args = example_args()
        args.read(iprot)
        iprot.readMessageEnd()
        result = example_result()
        try:
            result.success = self._handler.example()
            msg_type = TMessageType.REPLY
        except TTransport.TTransportException:
            raise
        except ExpectedException as exc:
            msg_type = TMessageType.REPLY
            result.exc = exc
        except TApplicationException as ex:
            logging.exception("TApplication exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = ex
        except Exception:
            logging.exception("Unexpected exception in handler")
            msg_type = TMessageType.EXCEPTION
            result = TApplicationException(TApplicationException.INTERNAL_ERROR, "Internal error")
        oprot.writeMessageBegin("example", msg_type, seqid)
        result.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES


class example_args(object):

    __slots__ = ()

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("example_args")
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


all_structs.append(example_args)
example_args.thrift_spec = ()


class example_result(object):
    """
    Attributes:
     - success
     - exc

    """

    __slots__ = ("success", "exc")

    def __init__(self, success=None, exc=None):
        self.success = success
        self.exc = exc

    def read(self, iprot):
        if (
            iprot._fast_decode is not None
            and isinstance(iprot.trans, TTransport.CReadableTransport)
            and self.thrift_spec is not None
        ):
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 0:
                if ftype == TType.BOOL:
                    self.success = iprot.readBool()
                else:
                    iprot.skip(ftype)
            elif fid == 1:
                if ftype == TType.STRUCT:
                    self.exc = ExpectedException()
                    self.exc.read(iprot)
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin("example_result")
        if self.success is not None:
            oprot.writeFieldBegin("success", TType.BOOL, 0)
            oprot.writeBool(self.success)
            oprot.writeFieldEnd()
        if self.exc is not None:
            oprot.writeFieldBegin("exc", TType.STRUCT, 1)
            self.exc.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ["%s=%r" % (key, getattr(self, key)) for key in self.__slots__]
        return "%s(%s)" % (self.__class__.__name__, ", ".join(L))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        for attr in self.__slots__:
            my_val = getattr(self, attr)
            other_val = getattr(other, attr)
            if my_val != other_val:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)


all_structs.append(example_result)
example_result.thrift_spec = (
    (0, TType.BOOL, "success", None, None),  # 0
    (1, TType.STRUCT, "exc", [ExpectedException, None], None),  # 1
)
fix_spec(all_structs)
del all_structs
