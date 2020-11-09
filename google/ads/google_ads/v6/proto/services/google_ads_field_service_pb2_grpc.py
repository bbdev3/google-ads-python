# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import google_ads_field_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_google__ads__field__pb2
from google.ads.google_ads.v6.proto.services import google_ads_field_service_pb2 as google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2


class GoogleAdsFieldServiceStub(object):
    """Proto file describing the GoogleAdsFieldService

    Service to fetch Google Ads API fields.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetGoogleAdsField = channel.unary_unary(
                '/google.ads.googleads.v6.services.GoogleAdsFieldService/GetGoogleAdsField',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.GetGoogleAdsFieldRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_google__ads__field__pb2.GoogleAdsField.FromString,
                )
        self.SearchGoogleAdsFields = channel.unary_unary(
                '/google.ads.googleads.v6.services.GoogleAdsFieldService/SearchGoogleAdsFields',
                request_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.SearchGoogleAdsFieldsRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.SearchGoogleAdsFieldsResponse.FromString,
                )


class GoogleAdsFieldServiceServicer(object):
    """Proto file describing the GoogleAdsFieldService

    Service to fetch Google Ads API fields.
    """

    def GetGoogleAdsField(self, request, context):
        """Returns just the requested field.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchGoogleAdsFields(self, request, context):
        """Returns all fields that match the search query.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GoogleAdsFieldServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetGoogleAdsField': grpc.unary_unary_rpc_method_handler(
                    servicer.GetGoogleAdsField,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.GetGoogleAdsFieldRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_google__ads__field__pb2.GoogleAdsField.SerializeToString,
            ),
            'SearchGoogleAdsFields': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchGoogleAdsFields,
                    request_deserializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.SearchGoogleAdsFieldsRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.SearchGoogleAdsFieldsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.GoogleAdsFieldService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GoogleAdsFieldService(object):
    """Proto file describing the GoogleAdsFieldService

    Service to fetch Google Ads API fields.
    """

    @staticmethod
    def GetGoogleAdsField(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.GoogleAdsFieldService/GetGoogleAdsField',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.GetGoogleAdsFieldRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_resources_dot_google__ads__field__pb2.GoogleAdsField.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchGoogleAdsFields(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.GoogleAdsFieldService/SearchGoogleAdsFields',
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.SearchGoogleAdsFieldsRequest.SerializeToString,
            google_dot_ads_dot_googleads__v6_dot_proto_dot_services_dot_google__ads__field__service__pb2.SearchGoogleAdsFieldsResponse.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
