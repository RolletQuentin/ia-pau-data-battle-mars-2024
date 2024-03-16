import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React from "react";
import SubSolutionDisplay from "./SubSolutionDisplay";

const SolutionDisplay = () => {
  // content customisation variable
  const topHeaderText = "Estimation des gains";

  // css customisation variable
  const backgroundColor = "#ededed";
  const backgroundColorAlpha = "a3";
  const textColor = "var(--dark-primary)";
  const titleFontSize = 20;
  const topHeaderFontSize = 30;
  const subSectionFontSize = 15;
  const globalMargin = "20px";
  const titleFontWeight = "bold";
  const subSectionFontWeight = "bold";
  const gap = "20px";
  const borderRadius = "20px";

  const percentageSplit = [11, 30, 20, 10, 10, 10, 9];

  const subSectionBoxShadow = "0px 4px 4px 0px #00000040";

  // css auto variable
  const mainBorderRadius =
    borderRadius + " 0px " + borderRadius + " " + borderRadius;
  const headerBorderRadius = borderRadius + " 0px 0px 0px";
  const topHeaderBorderRadius = borderRadius + " " + borderRadius + " 0px 0px";

  return (
    <VBox
      style={{
        width: "85vw",
      }}
    >
      <HBox justifyContent="end">
        <ColorRect
          backgroundColor={backgroundColor + backgroundColorAlpha}
          style={{
            borderRadius: topHeaderBorderRadius,
            width: "60%",
          }}
        >
          <MarginContainer margin={globalMargin}>
            <Text
              text={topHeaderText}
              color={textColor}
              fontWeight={titleFontWeight}
              fontSize={topHeaderFontSize}
            />
          </MarginContainer>
        </ColorRect>
      </HBox>
      <ColorRect
        backgroundColor={backgroundColor + backgroundColorAlpha}
        style={{
          borderRadius: mainBorderRadius,
        }}
      >
        <VBox>
          <ColorRect
            backgroundColor={backgroundColor}
            style={{
              boxShadow: subSectionBoxShadow,
              borderRadius: headerBorderRadius,
            }}
          >
            <MarginContainer margin={globalMargin}>
              <HBox gap={gap}>
                <Text
                  text="N* solution"
                  color={textColor}
                  fontWeight={titleFontWeight}
                  fontSize={titleFontSize + "px"}
                  style={{
                    width: "calc(" + percentageSplit[0] + "% - " + gap + ")",
                    textAlign: "left",
                  }}
                />
                <Text
                  text="Titre solution"
                  color={textColor}
                  fontWeight={titleFontWeight}
                  fontSize={titleFontSize + "px"}
                  style={{
                    width: "calc(" + percentageSplit[1] + "% - " + gap + ")",
                    textAlign: "left",
                  }}
                />
                <Text
                  text="Degré confiance"
                  color={textColor}
                  fontWeight={titleFontWeight}
                  fontSize={titleFontSize + "px"}
                  style={{
                    width: "calc(" + percentageSplit[2] + "% - " + gap + ")",
                    textAlign: "left",
                  }}
                />
                <Text
                  text="€"
                  color={textColor}
                  fontWeight={titleFontWeight}
                  fontSize={titleFontSize + "px"}
                  style={{
                    width: "calc(" + percentageSplit[3] + "% - " + gap + ")",
                    textAlign: "left",
                  }}
                />
                <Text
                  text="GWh/an"
                  color={textColor}
                  fontWeight={titleFontWeight}
                  fontSize={titleFontSize + "px"}
                  style={{
                    width: "calc(" + percentageSplit[4] + "% - " + gap + ")",
                    textAlign: "left",
                  }}
                />
                <Text
                  text="CO2"
                  color={textColor}
                  fontWeight={titleFontWeight}
                  fontSize={titleFontSize + "px"}
                  style={{
                    width: "calc(" + percentageSplit[5] + "% - " + gap + ")",
                    textAlign: "left",
                  }}
                />
              </HBox>
            </MarginContainer>
          </ColorRect>
          <SubSolutionDisplay
            margin={globalMargin}
            textColor={textColor}
            fontSize={subSectionFontSize}
            fontWeight={subSectionFontWeight}
            percentageSplit={percentageSplit}
          />
          <SubSolutionDisplay
            margin={globalMargin}
            textColor={textColor}
            fontSize={subSectionFontSize}
            fontWeight={subSectionFontWeight}
            percentageSplit={percentageSplit}
          />
          <SubSolutionDisplay
            margin={globalMargin}
            textColor={textColor}
            fontSize={subSectionFontSize}
            fontWeight={subSectionFontWeight}
            percentageSplit={percentageSplit}
          />
        </VBox>
      </ColorRect>
    </VBox>
  );
};

export default SolutionDisplay;
