import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useRef } from "react";
import SubSolutionDisplay from "./SubSolutionDisplay";
import CustomScrollBar from "./input/CustomScrollBar";

const SolutionDisplay = () => {
  // content customisation variable
  const topHeaderText = "Estimation des gains";
  const HeaderTitles = [
    "N°",
    "Titre",
    "Degré de confiance",
    "€",
    "GWh/an",
    "CO2",
  ];

  // css customisation variable
  const backgroundColor = "#ededed";
  const backgroundColorAlpha = "a3";
  const textColor = "var(--dark-primary)";
  const titleFontSize = 20;
  const topHeaderFontSize = 30;
  const subSectionFontSize = 15;
  const globalMargin = "15px";
  const titleFontWeight = "bold";
  const subSectionFontWeight = "bold";
  const gap = "20px";
  const borderRadius = "20px";

  const percentageSplit = [5, 35, 20, 11, 10, 10, 9];

  const subSectionBoxShadow = "0px 4px 4px 0px #00000040";

  // css auto variable
  const mainBorderRadius =
    borderRadius + " 0px " + borderRadius + " " + borderRadius;
  const headerBorderRadius = borderRadius + " 0px 0px 0px";
  const topHeaderBorderRadius = borderRadius + " " + borderRadius + " 0px 0px";

  const parentRef = useRef(null);
  const childRef = useRef(null);
  const scrollbarRef = useRef(null);

  const handleChildScroll = () => {
    if (scrollbarRef.current) {
      scrollbarRef.current.handleChildScroll();
    }
  };

  return (
    <HBox
      gap={gap}
      style={{
        width: "85vw",
        position: "relative",
      }}
    >
      <div ref={parentRef} style={{ flexGrow: 1 }}>
        <VBox mainBoxStyle={{ width: "100%" }}>
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
                    {HeaderTitles.map((title, index) => {
                      return (
                        <Text
                          key={index}
                          text={title}
                          color={textColor}
                          fontWeight={titleFontWeight}
                          fontSize={titleFontSize + "px"}
                          style={{
                            width:
                              "calc(" +
                              percentageSplit[index] +
                              "% - " +
                              gap +
                              ")",
                            textAlign: "left",
                          }}
                        />
                      );
                    })}
                  </HBox>
                </MarginContainer>
              </ColorRect>
              <div style={{ overflow: "hidden", height: "300px" }}>
                <div
                  style={{
                    height: "300px",
                    overflowY: "scroll",
                    marginRight: "-20px", // Adjust for scrollbar width
                  }}
                  onScroll={handleChildScroll}
                  ref={childRef}
                >
                  <VBox>
                    {Array.from({ length: 40 }).map((_, index) => (
                      <SubSolutionDisplay
                        key={index}
                        margin={globalMargin}
                        textColor={textColor}
                        fontSize={subSectionFontSize}
                        fontWeight={subSectionFontWeight}
                        percentageSplit={percentageSplit}
                      />
                    ))}
                  </VBox>
                </div>
              </div>
            </VBox>
          </ColorRect>
        </VBox>
      </div>
      <CustomScrollBar
        ref={scrollbarRef}
        parentRef={parentRef}
        childRef={childRef}
        ThumbColor="var(--dark-primary)"
        backgroundColor={backgroundColor + backgroundColorAlpha}
      />
    </HBox>
  );
};

export default SolutionDisplay;
