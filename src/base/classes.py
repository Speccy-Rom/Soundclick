class MixedSerializer:
    """Serializer action's mixin"""

    def get_serializer(self, *args, **kwargs):
        try:
            serializer_class = self.serializer_classes_by_action[self.action]
        except KeyError:
            serializer_class = self.get_serializer_class()
        kwargs.setdefault('contex', self.get_serializer_context())
        return serializer_class(*args, **kwargs)
