import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useEffect, useRef } from "react";
import SubSolutionDisplay from "./SubSolutionDisplay";
import CustomScrollBar from "./input/CustomScrollBar";

const SolutionDisplay = ({
  solutions,
  // css customisation variable
  backgroundColor = "#ededed",
  backgroundColorAlpha = "a3",
  backgroundBlur = "blur(20px)",
  titleFontSize = 20,
  textColor = "var(--dark-primary)",
  subSectionFontSize = 15,
  globalMargin = "15px",
  titleFontWeight = "bold",
  borderRadius = "20px",
  backgroundColorAlphaTopHeader = "a3",
  topHeaderFontSize = 30,
  subSectionBoxShadow = "0px 4px 4px 0px #00000040",
  gap = "20px",
  subSectionFontWeight = "bold",
  percentageSplit = [5, 35, 20, 11, 10, 10, 9],
  // content customisation variable
  topHeaderText = "Estimation des gains",
  HeaderTitles = ["N°", "Titre", "Degré de confiance", "€", "GWh/an", "CO2"],
}) => {
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

  useEffect(() => {
    if (scrollbarRef.current) {
      scrollbarRef.current.refresh();
    }
  }, [solutions]);

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
              backgroundColor={backgroundColor + backgroundColorAlphaTopHeader}
              style={{
                borderRadius: topHeaderBorderRadius,
                width: "60%",
                backdropFilter: backgroundBlur,
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
              backdropFilter: backgroundBlur,
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
                    {solutions.map((solution, index) => (
                      <SubSolutionDisplay
                        key={index}
                        margin={globalMargin}
                        textColor={textColor}
                        fontSize={subSectionFontSize}
                        fontWeight={subSectionFontWeight}
                        percentageSplit={percentageSplit}
                        solution={solution}
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
        backgroundColor={backgroundColor}
      />
    </HBox>
  );
};

export default SolutionDisplay;
