import {
  CenterContainer,
  MarginContainer,
  Text,
  TextureRect,
  VBox,
} from "@liro_u/react-components";
import React from "react";
import Footer from "../Components/Footer";
import SolutionFinder from "../Components/SolutionFinder";

const Home = () => {
  // content customisation variable
  const backgroundImageSrc = "/wallpaper/forest.jpg";
  const topTextList = [
    "Réduisez vos émissions de CO2 et faites des économies !",
    "Nous avons les solutions faites sur-mesure pour vous !",
  ];

  // css customisation variable
  const verticalMargin = "100px";
  const horizontalMargin = "200px";
  const textFontWeight = "bold";
  const textFontSize = "35px";
  const gap = "70px";

  return (
    <MarginContainer
      style={{ minHeight: "100%", display: "flex", flexDirection: "column" }}
    >
      <TextureRect texture={backgroundImageSrc} style={{ flexGrow: "1" }}>
        <MarginContainer
          margin={verticalMargin}
          marginLeft={horizontalMargin}
          marginRight={horizontalMargin}
        >
          <VBox gap={gap}>
            <CenterContainer>
              <VBox>
                {topTextList.map((value, index) => {
                  return (
                    <Text
                      text={value}
                      key={index}
                      fontWeight={textFontWeight}
                      fontSize={textFontSize}
                      style={{ textShadow: "1px 1px 2px black" }}
                    />
                  );
                })}
              </VBox>
            </CenterContainer>
            <CenterContainer>
              <SolutionFinder />
            </CenterContainer>
          </VBox>
        </MarginContainer>
      </TextureRect>
      <Footer />
    </MarginContainer>
  );
};

export default Home;
