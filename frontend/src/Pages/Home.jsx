import {
  CenterContainer,
  HBox,
  MarginContainer,
  Text,
  TextureRect,
  VBox,
} from "@liro_u/react-components";
import React, { useState } from "react";
import Footer from "../Components/Footer";
import SolutionFinder from "../Components/SolutionFinder";
import SolutionDisplay from "../Components/SolutionDisplay";
import { Opacity } from "@liro_u/react-animation-components";
import CustomButton from "../Components/input/CustomButton";

const Home = () => {
  const [pageState, setPageState] = useState(0);
  const [windowJustOpened, setWindowJustOpen] = useState(true);
  const [solutions, setSolutions] = useState([]);

  // content customisation variable
  const backgroundImageSrc = "/wallpaper/forest.jpg";
  const topTextList = [
    "Réduisez vos émissions de CO2 et faites des économies !",
    "Nous avons les solutions faites sur-mesure pour vous !",
  ];

  // css customisation variable
  const verticalMargin = "50px";
  const horizontalMargin = "200px";
  const textFontWeight = "bold";
  const textFontSize = "35px";
  const gap = "70px";

  // css animation
  const show = `
    @keyframes show {
      0% {
        transform: translate(0, 100vh) perspective(300px) rotateX(45deg) scale(0.5, 1);
      }
      100% {
        transform: translate(0, 0) perspective(300px) rotateX(0) scale(1, 1);
      }
    }
  `;

  const hide = `
    @keyframes hide {
      0% {
        transform: translate(0, 0) perspective(300px) rotateX(0) scale(1, 1);
      }
      100% {
        transform: translate(0, 100vh) perspective(300px) rotateX(45deg) scale(0.5, 1);
      }
    }
  `;

  const startingSolutionDisplay = `
    @keyframes startingSolutionDisplay {
      0% {
        transform: translate(0, 100vh);
      }
      100% {
        transform: translate(0, 100vh);
      }
    }
  `;

  // functions
  const findSolutions = (s) => {
    setSolutions(s);
    setPageState(2);
    if (windowJustOpened) {
      setWindowJustOpen(false);
    }
  };

  const goBackToSearch = () => {
    setPageState(1);
  };

  return (
    <MarginContainer
      style={{
        maxHeight: "100%",
        minHeight: "100%",
        display: "flex",
        flexDirection: "column",
      }}
    >
      <style>{hide}</style>
      <style>{show}</style>
      <style>{startingSolutionDisplay}</style>
      <TextureRect
        texture={backgroundImageSrc}
        style={{ flexGrow: "1", overflow: "hidden", display: "flex" }}
      >
        <MarginContainer
          margin={verticalMargin}
          marginLeft={horizontalMargin}
          marginRight={horizontalMargin}
          style={{
            flexGrow: 1,
            display: "flex",
          }}
        >
          <HBox
            justifyContent="center"
            style={{ position: "relative", flexGrow: 1 }}
          >
            <VBox
              gap={gap}
              mainBoxStyle={{
                position: "absolute",
                animationName: pageState === 0 ? "show" : "hide",
                animationDuration: "0.5s",
                animationFillMode: "forwards",
                height: "80vh",
              }}
            >
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
                <CustomButton
                  buttonWidth="300px"
                  text="Découvrir comment"
                  fontSize={20}
                  verticalMargin={25}
                  buttonColor="var(--dark-primary2)"
                  buttonColorHover="var(--dark-primary)"
                  onClick={goBackToSearch}
                />
              </CenterContainer>
            </VBox>
            <VBox
              gap={gap}
              mainBoxStyle={{
                position: "absolute",
                animationName:
                  pageState === 0
                    ? "startingSolutionDisplay"
                    : pageState === 1
                    ? "show"
                    : "hide",
                animationDuration: "0.5s",
                animationFillMode: "forwards",
                height: "80vh",
              }}
            >
              <CenterContainer>
                <SolutionFinder callBack={findSolutions} />
              </CenterContainer>
            </VBox>
            <VBox
              gap={gap}
              mainBoxStyle={{
                position: "absolute",
                animationName: windowJustOpened
                  ? "startingSolutionDisplay"
                  : pageState === 2
                  ? "show"
                  : "hide",
                animationDuration: "0.5s",
                animationFillMode: "forwards",
                height: "80vh",
              }}
            >
              <Opacity
                opacityStart={"0"}
                opacityEnd={"1"}
                delay={"200"}
                time={"0.7"}
              >
                <CenterContainer>
                  <i
                    style={{
                      border: "solid black",
                      borderWidth: "0 5px 5px 0",
                      display: "inline-block",
                      padding: "10px",
                      borderColor: "var(--light-color)",
                      transform: "rotate(-135deg)",
                      cursor: "pointer",
                    }}
                    onClick={goBackToSearch}
                  />
                </CenterContainer>
              </Opacity>
              <CenterContainer>
                <SolutionDisplay solutions={solutions} />
              </CenterContainer>
            </VBox>
          </HBox>
        </MarginContainer>
      </TextureRect>
      <Footer />
    </MarginContainer>
  );
};

export default Home;
