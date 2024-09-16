from pydantic import BaseModel, Field
from spacy.tokens import Doc


class ProductDescription(BaseModel):
    title: str


class ExtractedProductInformation(BaseModel):
    """
    A class to represent the extracted product information.
    alias is used to convert snake_case to camelCase when serializing into JSON.
    """

    brand: str | None = Field(None, alias="brand")
    storage_capacity: str | None = Field(None, alias="storageCapacity")
    color: str | None = Field(None, alias="color")

    @classmethod
    def from_spacy_output(cls, output: Doc) -> "ExtractedProductInformation":
        brand, storage_capacity, color = None, None, None
        for ent in output.ents:
            match ent.label_:
                case "Brand":
                    brand = ent.text
                case "Storage":
                    storage_capacity = ent.text
                case "Color":
                    color = ent.text
                case _:
                    pass

        return cls(brand=brand, storageCapacity=storage_capacity, color=color)
