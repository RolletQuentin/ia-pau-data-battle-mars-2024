import { ColorRect, MarginContainer, Text } from "@liro_u/react-components";
import React, { useState } from "react";

const CustomButton = ({
  buttonWidth = "30%",
  buttonColor = "var(--dark-primary)",
  buttonColorHover = "var(--dark-primary2)",
  textColor = "var(--light-color)",
  textFontWeight = "bold",
  text = "send",
  borderRadius = "20px",
  onClick = () => {},
  boxShadow = "0px 4px 4px 0px #00000040",
  verticalMargin = 5,
  fontSize = 15,
  horizontalMargin = fontSize,
  transition = "background-size 0.5s",
  backgroundPosition = "50% 50%",
  ...content
}) => {
  const backgroundImage =
    "linear-gradient(" + buttonColorHover + ", " + buttonColorHover + ")";

  const [isHovered, setIsHovered] = useState(false);

  const handleMouseEnter = () => {
    setIsHovered(true);
  };

  const handleMouseLeave = () => {
    setIsHovered(false);
  };

  return (
    <ColorRect
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      backgroundColor={buttonColor}
      style={{
        borderRadius,
        width: buttonWidth,
        boxShadow: boxShadow,
        cursor: "pointer",
        backgroundImage,
        transition,
        backgroundRepeat: "no-repeat",
        backgroundPosition,
        backgroundSize: (isHovered ? "100%" : "0%") + " 100%",
        height: "fit-content",
      }}
      onClick={onClick}
      {...content}
    >
      <MarginContainer
        margin={verticalMargin + "px"}
        marginLeft={horizontalMargin + "px"}
        marginRight={horizontalMargin + "px"}
      >
        <Text
          text={text}
          color={textColor}
          fontSize={fontSize + "px"}
          fontWeight={textFontWeight}
        />
      </MarginContainer>
    </ColorRect>
  );
};

export default CustomButton;
