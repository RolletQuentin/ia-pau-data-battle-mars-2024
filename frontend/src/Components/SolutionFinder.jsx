import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useState } from "react";
import TextArea from "./input/TextArea";

const SolutionFinder = () => {
  // content customisation variable
  const section2Text = "Description";
  const section1Text = "Secteur d'activité";
  const validateButtonText = "Mes solutions";
  const descriptionTextPlaceholder =
    "Exemple : Mettre en transparance un exemple bien détaillé de ce que l’user doit écrire dans cette section. Comme ça on augmente les chances qu’il écrive pas n’importe quoi.";

  // css customisation variable
  const backgroundColor = "#ededed";
  const backgroundColorAlpha = "e3";
  const textColor = "var(--dark-primary)";
  const titleFontSize = 20;
  const subSectionFontSize = 15;
  const borderRadius = "30px";
  const globalMargin = "50px";
  const titleFontWeight = "bold";
  const gap = "20px";
  const subSectionPercentage = "70%";
  const subSectionBorderRadius = "20px";
  const validateButtonWidth = "30%";
  const validateButtonColor = "var(--dark-primary)";
  const validateButtonTextColor = "var(--light-color)";
  const validateButtonTextFontWeight = "bold";
  const subSectionBoxShadow = "0px 4px 4px 0px #00000040";

  // css auto variable
  const subSectionVerticalMargin = titleFontSize - subSectionFontSize;
  const subSectionHorizontalMargin = subSectionFontSize;

  // react update variable
  const [description, setDescription] = useState("");

  // API call
  const askAPIForSolutions = () => {
    console.log("asking api for solutions");
  };

  return (
    <ColorRect
      backgroundColor={backgroundColor + backgroundColorAlpha}
      style={{ borderRadius, width: "50vw", boxShadow: subSectionBoxShadow }}
    >
      <MarginContainer margin={globalMargin}>
        <VBox gap={gap}>
          <HBox justifyContent="space-between">
            <Text
              text={section1Text}
              color={textColor}
              fontWeight={titleFontWeight}
              fontSize={titleFontSize + "px"}
            />
            <ColorRect
              backgroundColor={backgroundColor}
              style={{
                borderRadius: subSectionBorderRadius,
                width: subSectionPercentage,
                boxShadow: subSectionBoxShadow,
              }}
            >
              <MarginContainer
                margin={subSectionVerticalMargin + "px"}
                marginLeft={subSectionHorizontalMargin + "px"}
                marginRight={subSectionHorizontalMargin + "px"}
              >
                <HBox justifyContent="space-between">
                  <Text
                    text="drop menu"
                    color={textColor}
                    fontSize={subSectionFontSize + "px"}
                  />
                  <Text
                    text="\/"
                    color={textColor}
                    fontSize={subSectionFontSize + "px"}
                  />
                </HBox>
              </MarginContainer>
            </ColorRect>
          </HBox>
          <HBox justifyContent="space-between">
            <Text
              text={section2Text}
              color={textColor}
              fontWeight={titleFontWeight}
              fontSize={titleFontSize + "px"}
            />
            <ColorRect
              backgroundColor={backgroundColor}
              style={{
                borderRadius: subSectionBorderRadius,
                width: subSectionPercentage,
                height: "100px",
                boxShadow: subSectionBoxShadow,
              }}
            >
              <TextArea
                placeholder={descriptionTextPlaceholder}
                color={textColor}
                setValue={setDescription}
                value={description}
                style={{
                  backgroundColor: "#0000",
                  padding: subSectionVerticalMargin + "px",
                  paddingRight: subSectionHorizontalMargin + "px",
                  paddingLeft: subSectionHorizontalMargin + "px",
                  borderRadius: subSectionBorderRadius,
                  width:
                    "calc(100% - " + subSectionHorizontalMargin * 2 + "px)",
                  height: "calc(100% - " + subSectionVerticalMargin * 2 + "px)",
                }}
              />
            </ColorRect>
          </HBox>
          <HBox justifyContent="right">
            <ColorRect
              backgroundColor={validateButtonColor}
              style={{
                borderRadius: subSectionBorderRadius,
                width: validateButtonWidth,
                boxShadow: subSectionBoxShadow,
                cursor: "pointer",
              }}
              onClick={askAPIForSolutions}
            >
              <MarginContainer
                margin={subSectionVerticalMargin + "px"}
                marginLeft={subSectionHorizontalMargin + "px"}
                marginRight={subSectionHorizontalMargin + "px"}
              >
                <Text
                  text={validateButtonText}
                  color={validateButtonTextColor}
                  fontSize={subSectionFontSize + "px"}
                  fontWeight={validateButtonTextFontWeight}
                />
              </MarginContainer>
            </ColorRect>
          </HBox>
        </VBox>
      </MarginContainer>
    </ColorRect>
  );
};

export default SolutionFinder;
