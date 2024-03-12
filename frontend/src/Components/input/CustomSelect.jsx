import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
} from "@liro_u/react-components";
import React from "react";

const CustomSelect = ({
  backgroundColor = "#ededed",
  borderRadius = "20px",
  boxShadow = "0px 4px 4px 0px #00000040",
  width = "70%",
  verticalMargin = 5,
  textColor = "var(--dark-primary)",
  fontSize = 15,
  horizontalMargin = fontSize,
}) => {
  return (
    <ColorRect
      backgroundColor={backgroundColor}
      style={{
        borderRadius,
        width,
        boxShadow,
        cursor: "pointer",
      }}
    >
      <MarginContainer
        margin={verticalMargin + "px"}
        marginLeft={horizontalMargin + "px"}
        marginRight={horizontalMargin + "px"}
      >
        <HBox justifyContent="space-between">
          <Text text="drop menu" color={textColor} fontSize={fontSize + "px"} />
          <Text
            text="\/"
            color={textColor}
            fontSize={fontSize + "px"}
            style={{
              userSelect: "none",
            }}
          />
        </HBox>
      </MarginContainer>
    </ColorRect>
  );
};

export default CustomSelect;
