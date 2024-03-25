import { ColorRect, MarginContainer, Text } from "@liro_u/react-components";
import React, { useState } from "react";

const CustomButton = ({
  buttonWidth = "30%",
  buttonColor = "var(--dark-primary)",
  buttonColorHover = "var(--dark-primary2)",
  buttonDisableColor = "var(--disable)",
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
  isDisable = false,
  ...content
}) => {
  const backgroundImage =
    "linear-gradient(" + buttonColorHover + ", " + buttonColorHover + ")";

  const backgroundImageDisable =
    "linear-gradient(" + buttonDisableColor + ", " + buttonDisableColor + ")";

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
      backgroundColor={isDisable ? buttonDisableColor : buttonColor}
      style={{
        borderRadius,
        width: buttonWidth,
        boxShadow: boxShadow,
        cursor: isDisable ? "wait" : "pointer",
        backgroundImage: isDisable ? backgroundImageDisable : backgroundImage,
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
