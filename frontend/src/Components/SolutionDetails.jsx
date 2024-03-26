import {
  CenterContainer,
  ColorRect,
  HBox,
  Image,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useEffect, useRef } from "react";
import CustomScrollBar from "./input/CustomScrollBar";

import { useTranslation } from "react-i18next";
import Tableau from "./Tableau";

const SolutionDetails = ({
  gap = "20px",
  textGap = "10px",
  backgroundColor = "#ededed",
  backgroundColorAlpha = "a3",
  borderRadius = "20px",
  globalMargin = "15px",
  backgroundBlur = "blur(20px)",
  subGap = "10px",
  subSectionFontSize = 15,
  subSectionBoxShadow = "0px 4px 4px 0px #00000040",
  textColor = "var(--dark-primary)",
  negativeTextColor = "var(--light-color)",
  titleFontWeight = "bold",
  titleFontSize = 20,
  lineHeight = "2px",
  lineMargin = "20px",
  estimPersoGainMargin = "30px",
  estimGenGainMargin = "30px",
  badBackgroundColor = "var(--error)",
  orangeBackgroundColor = "var(--orange)",
  solutionData = {
    numSolution: 54,
    titleSolution: "truc",
    technologie: "truc",
    definition: null,
    application: null,
    bilanEnergie: null,
    estimPersoGain: null,
    estimGenGain: {
      cout: {
        pouce: null,
        difficulte: [],
      },
      gain: {
        gain: null,
        positif: [],
      },
    },
    etudeCas: [],
  },
}) => {
  const { t } = useTranslation();

  // css auto variable
  const headerBorderRadius = borderRadius + " " + borderRadius + " 0px 0px";

  // text variable
  const titleSolutionData = {
    numSolution: t("solutionDetail.numSolution"),
    titleSolution: t("solutionDetail.titleSolution"),
    technologie: t("solutionDetail.technologie"),
    definition: t("solutionDetail.definition"),
    application: t("solutionDetail.application"),
    bilanEnergie: t("solutionDetail.bilanEnergie"),
    estimPersoGain: {
      title: t("solutionDetail.estimPersoGain.title"),
      degConf: t("solutionDetail.estimPersoGain.degConf"),
      euro: t("solutionDetail.estimPersoGain.euro"),
      gwh: t("solutionDetail.estimPersoGain.gwh"),
      co2: t("solutionDetail.estimPersoGain.co2"),
      gainReel: t("solutionDetail.estimPersoGain.gainReel"),
      retourInv: t("solutionDetail.estimPersoGain.retourInv"),
      coutFinance: t("solutionDetail.estimPersoGain.coutFinance"),
    },
    estimGenGain: {
      title: t("solutionDetail.estimGenGain.title"),
      cout: {
        title: t("solutionDetail.estimGenGain.cout.title"),
        pouce: t("solutionDetail.estimGenGain.cout.pouce"),
        difficulte: t("solutionDetail.estimGenGain.cout.difficulte"),
      },
      gain: {
        title: t("solutionDetail.estimGenGain.gain.title"),
        gain: t("solutionDetail.estimGenGain.gain.gain"),
        positif: t("solutionDetail.estimGenGain.gain.positif"),
      },
    },
    etudeCas: {
      title: t("solutionDetail.etudeCas.title"),
      sub1: t("solutionDetail.etudeCas.sub1"),
      sub2: t("solutionDetail.etudeCas.sub2"),
      sub3: t("solutionDetail.etudeCas.sub3"),
    },
  };

  const parentRef = useRef(null);
  const childRef = useRef(null);
  const scrollbarRef = useRef(null);

  useEffect(() => {
    if (scrollbarRef.current) {
      scrollbarRef.current.refresh();
    }
  }, [solutionData]);

  const handleChildScroll = () => {
    if (scrollbarRef.current) {
      scrollbarRef.current.handleChildScroll();
    }
  };

  return (
    <HBox
      gap={gap}
      style={{
        width: "95vw",
        position: "relative",
      }}
    >
      <div ref={parentRef} style={{ flexGrow: 1 }}>
        <VBox mainBoxStyle={{ width: "100%" }}>
          <ColorRect
            backgroundColor={backgroundColor + backgroundColorAlpha}
            style={{
              borderRadius: borderRadius,
              backdropFilter: backgroundBlur,
            }}
          >
            <VBox>
              <ColorRect
                backgroundColor={backgroundColor}
                style={{
                  zIndex: "2",
                  position: "relative",
                  boxShadow: subSectionBoxShadow,
                  borderRadius: headerBorderRadius,
                }}
              >
                <MarginContainer margin={globalMargin}>
                  <HBox gap={gap}>
                    <VBox mainBoxStyle={{ width: "50%" }}>
                      <HBox
                        gap={textGap}
                        style={{ height: "min-content", overflow: "hidden" }}
                      >
                        <Text
                          text={titleSolutionData.numSolution}
                          color={textColor}
                          fontWeight={titleFontWeight}
                          fontSize={titleFontSize + "px"}
                          textWrap="nowrap"
                          style={{
                            textAlign: "left",
                          }}
                        />
                        <Text
                          text={solutionData.numSolution}
                          color={textColor}
                          textWrap="nowrap"
                          fontSize={titleFontSize + "px"}
                          textOverflow="ellipsis"
                          style={{
                            textAlign: "left",
                            flexGrow: 1,
                            overflow: "hidden",
                          }}
                        />
                      </HBox>
                      <HBox
                        gap={textGap}
                        style={{ height: "min-content", overflow: "hidden" }}
                      >
                        <Text
                          text={titleSolutionData.titleSolution}
                          color={textColor}
                          fontWeight={titleFontWeight}
                          textWrap="nowrap"
                          fontSize={titleFontSize + "px"}
                          style={{
                            textAlign: "left",
                          }}
                        />
                        <Text
                          text={solutionData.titleSolution}
                          color={textColor}
                          fontSize={titleFontSize + "px"}
                          textWrap="nowrap"
                          textOverflow="ellipsis"
                          style={{
                            textAlign: "left",
                            flexGrow: 1,
                            overflow: "hidden",
                          }}
                        />
                      </HBox>
                    </VBox>
                    <VBox>
                      <HBox
                        gap={textGap}
                        style={{ height: "min-content", overflow: "hidden" }}
                      >
                        <Text
                          text={titleSolutionData.technologie}
                          color={textColor}
                          fontWeight={titleFontWeight}
                          fontSize={titleFontSize + "px"}
                          textWrap="nowrap"
                          style={{
                            textAlign: "left",
                          }}
                        />
                        <Text
                          text={solutionData.technologie}
                          color={textColor}
                          fontSize={titleFontSize + "px"}
                          textWrap="nowrap"
                          textOverflow="ellipsis"
                          style={{
                            textAlign: "left",
                            flexGrow: 1,
                            overflow: "hidden",
                          }}
                        />
                      </HBox>
                    </VBox>
                  </HBox>
                </MarginContainer>
              </ColorRect>
              <MarginContainer
                margin={globalMargin}
                marginTop="0"
                marginBottom="0"
              >
                <div style={{ overflow: "hidden", height: "550px" }}>
                  <div
                    style={{
                      height: "550px",
                      overflowY: "scroll",
                      marginRight: "-20px", // Adjust for scrollbar width
                    }}
                    onScroll={handleChildScroll}
                    ref={childRef}
                  >
                    <MarginContainer
                      marginTop={globalMargin}
                      marginRight="0"
                      marginLeft="0"
                    >
                      <VBox>
                        {solutionData.definition && (
                          <VBox>
                            <Text
                              text={titleSolutionData.definition}
                              color={textColor}
                              fontWeight={titleFontWeight}
                              fontSize={titleFontSize + "px"}
                              style={{
                                textAlign: "left",
                              }}
                            />
                            {solutionData.definition.map((d, index) => {
                              return (
                                <VBox key={index} gap={subGap}>
                                  {d.before && (
                                    <Text
                                      text={d.before}
                                      color={textColor}
                                      fontSize={subSectionFontSize + "px"}
                                      style={{
                                        textAlign: "left",
                                      }}
                                    />
                                  )}
                                  {d.tab && (
                                    <Tableau
                                      tab={d.tab}
                                      color={textColor}
                                      titleFontWeight={titleFontWeight}
                                      subSectionFontSize={subSectionFontSize}
                                      titleFontSize={titleFontSize}
                                    />
                                  )}
                                  {d.after && (
                                    <Text
                                      text={d.after}
                                      color={textColor}
                                      fontSize={subSectionFontSize + "px"}
                                      style={{
                                        textAlign: "left",
                                      }}
                                    />
                                  )}
                                </VBox>
                              );
                            })}
                            <MarginContainer
                              margin={lineMargin}
                              marginRight={"0"}
                              marginLeft={"0"}
                            >
                              <ColorRect
                                style={{ height: lineHeight }}
                                backgroundColor={textColor}
                              />
                            </MarginContainer>
                          </VBox>
                        )}
                        {solutionData.application && (
                          <VBox>
                            <Text
                              text={titleSolutionData.application}
                              color={textColor}
                              fontWeight={titleFontWeight}
                              fontSize={titleFontSize + "px"}
                              style={{
                                textAlign: "left",
                              }}
                            />
                            {solutionData.application.map((d, index) => {
                              return (
                                <VBox key={index} gap={subGap}>
                                  {d.before && (
                                    <Text
                                      text={d.before}
                                      color={textColor}
                                      fontSize={subSectionFontSize + "px"}
                                      style={{
                                        textAlign: "left",
                                      }}
                                    />
                                  )}
                                  {d.tab && (
                                    <Tableau
                                      tab={d.tab}
                                      color={textColor}
                                      titleFontWeight={titleFontWeight}
                                      subSectionFontSize={subSectionFontSize}
                                      titleFontSize={titleFontSize}
                                    />
                                  )}
                                  {d.after && (
                                    <Text
                                      text={d.after}
                                      color={textColor}
                                      fontSize={subSectionFontSize + "px"}
                                      style={{
                                        textAlign: "left",
                                      }}
                                    />
                                  )}
                                </VBox>
                              );
                            })}
                            <MarginContainer
                              margin={lineMargin}
                              marginRight={"0"}
                              marginLeft={"0"}
                            >
                              <ColorRect
                                style={{ height: lineHeight }}
                                backgroundColor={textColor}
                              />
                            </MarginContainer>
                          </VBox>
                        )}
                        {solutionData.bilanEnergie && (
                          <VBox>
                            <Text
                              text={titleSolutionData.bilanEnergie}
                              color={textColor}
                              fontWeight={titleFontWeight}
                              fontSize={titleFontSize + "px"}
                              style={{
                                textAlign: "left",
                              }}
                            />
                            {solutionData.bilanEnergie.map((d, index) => {
                              return (
                                <VBox key={index} gap={subGap}>
                                  {d.before && (
                                    <Text
                                      text={d.before}
                                      color={textColor}
                                      fontSize={subSectionFontSize + "px"}
                                      style={{
                                        textAlign: "left",
                                      }}
                                    />
                                  )}
                                  {d.tab && (
                                    <Tableau
                                      tab={d.tab}
                                      color={textColor}
                                      titleFontWeight={titleFontWeight}
                                      subSectionFontSize={subSectionFontSize}
                                      titleFontSize={titleFontSize}
                                    />
                                  )}
                                  {d.after && (
                                    <Text
                                      text={d.after}
                                      color={textColor}
                                      fontSize={subSectionFontSize + "px"}
                                      style={{
                                        textAlign: "left",
                                      }}
                                    />
                                  )}
                                </VBox>
                              );
                            })}
                            <MarginContainer
                              margin={lineMargin}
                              marginRight={"0"}
                              marginLeft={"0"}
                            >
                              <ColorRect
                                style={{ height: lineHeight }}
                                backgroundColor={textColor}
                              />
                            </MarginContainer>
                          </VBox>
                        )}
                        {solutionData.estimPersoGain && (
                          <VBox>
                            <VBox gap={subGap}>
                              <HBox gap={subGap}>
                                <Text
                                  text={titleSolutionData.estimPersoGain.title}
                                  color={textColor}
                                  fontWeight={titleFontWeight}
                                  fontSize={titleFontSize + "px"}
                                  style={{
                                    textAlign: "left",
                                  }}
                                />
                                <Image
                                  src="/icon/brain.png"
                                  objectFit="contain"
                                  width="30px"
                                  height="30px"
                                />
                              </HBox>
                              <HBox gap={gap}>
                                <VBox mainBoxStyle={{ width: "100%" }}>
                                  <HBox gap={gap}>
                                    <ColorRect
                                      backgroundColor={"var(--orange)"}
                                      style={{
                                        width:
                                          "calc(18% - calc(" + gap + " / 3))",
                                      }}
                                    >
                                      <MarginContainer
                                        margin={estimPersoGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <HBox>
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .degConf
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                            }}
                                          />
                                        </HBox>
                                      </MarginContainer>
                                    </ColorRect>

                                    <ColorRect
                                      backgroundColor={textColor}
                                      style={{
                                        width:
                                          "calc(67% - calc(" + gap + " / 3))",
                                      }}
                                    >
                                      <MarginContainer
                                        margin={estimPersoGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <HBox>
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .euro
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "18%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .gwh
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "17%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .co2
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "13%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .gainReel
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "15%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .retourInv
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "37%",
                                            }}
                                          />
                                        </HBox>
                                      </MarginContainer>
                                    </ColorRect>

                                    <ColorRect
                                      backgroundColor={"var(--error)"}
                                      style={{
                                        width:
                                          "calc(15% - calc(" + gap + " / 3))",
                                      }}
                                    >
                                      <MarginContainer
                                        margin={estimPersoGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <HBox>
                                          <Text
                                            text={
                                              titleSolutionData.estimPersoGain
                                                .coutFinance
                                            }
                                            color={negativeTextColor}
                                            fontWeight={titleFontWeight}
                                            fontSize={titleFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                            }}
                                          />
                                        </HBox>
                                      </MarginContainer>
                                    </ColorRect>
                                  </HBox>
                                  <HBox gap={gap}>
                                    <ColorRect
                                      backgroundColor={"#0000"}
                                      style={{
                                        width:
                                          "calc(18% - calc(" + gap + " / 3))",
                                      }}
                                    >
                                      <MarginContainer
                                        margin={estimPersoGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <HBox>
                                          <Text
                                            text={
                                              t("based_on") +
                                              " " +
                                              solutionData.estimPersoGain
                                                .degConf +
                                              " " +
                                              t("studies")
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                            }}
                                          />
                                        </HBox>
                                      </MarginContainer>
                                    </ColorRect>
                                    <ColorRect
                                      backgroundColor={"#0000"}
                                      style={{
                                        width:
                                          "calc(67% - calc(" + gap + " / 3))",
                                      }}
                                    >
                                      <MarginContainer
                                        margin={estimPersoGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <HBox>
                                          <Text
                                            text={
                                              solutionData.estimPersoGain.euro
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "18%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              solutionData.estimPersoGain.gwh
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "17%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              solutionData.estimPersoGain.co2
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "13%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              solutionData.estimPersoGain
                                                .gainReel
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "15%",
                                            }}
                                          />
                                          <Text
                                            text={
                                              solutionData.estimPersoGain
                                                .retourInv
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                              width: "37%",
                                            }}
                                          />
                                        </HBox>
                                      </MarginContainer>
                                    </ColorRect>
                                    <ColorRect
                                      backgroundColor={"#0000"}
                                      style={{
                                        width:
                                          "calc(15% - calc(" + gap + " / 3))",
                                      }}
                                    >
                                      <MarginContainer
                                        margin={estimPersoGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <HBox>
                                          <Text
                                            text={
                                              solutionData.estimPersoGain
                                                .coutFinance
                                            }
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                            }}
                                          />
                                        </HBox>
                                      </MarginContainer>
                                    </ColorRect>
                                  </HBox>
                                </VBox>
                              </HBox>
                            </VBox>

                            <MarginContainer
                              margin={lineMargin}
                              marginRight={"0"}
                              marginLeft={"0"}
                            >
                              <ColorRect
                                style={{ height: lineHeight }}
                                backgroundColor={textColor}
                              />
                            </MarginContainer>
                          </VBox>
                        )}
                        {(solutionData.estimGenGain.cout.jauge ||
                          solutionData.estimGenGain.cout.pouce ||
                          solutionData.estimGenGain.cout.difficulte.length >
                            0 ||
                          solutionData.estimGenGain.gain.jauge ||
                          solutionData.estimGenGain.gain.gain ||
                          solutionData.estimGenGain.gain.positif.length >
                            0) && (
                          <VBox>
                            <VBox gap={subGap}>
                              <Text
                                text={titleSolutionData.estimGenGain.title}
                                color={textColor}
                                fontWeight={titleFontWeight}
                                fontSize={titleFontSize + "px"}
                                style={{
                                  textAlign: "left",
                                }}
                              />
                              <HBox gap={gap}>
                                <VBox
                                  gap={subGap}
                                  mainBoxStyle={{
                                    width: "calc(50% - " + gap + ")",
                                  }}
                                >
                                  <ColorRect
                                    backgroundColor={badBackgroundColor}
                                  >
                                    <MarginContainer
                                      margin={estimGenGainMargin}
                                      marginTop={"0"}
                                      marginBottom={"0"}
                                    >
                                      <Text
                                        text={
                                          titleSolutionData.estimGenGain.cout
                                            .title
                                        }
                                        color={negativeTextColor}
                                        fontWeight={titleFontWeight}
                                        fontSize={titleFontSize + "px"}
                                        style={{
                                          textAlign: "left",
                                        }}
                                      />
                                    </MarginContainer>
                                  </ColorRect>
                                  <MarginContainer
                                    margin={estimGenGainMargin}
                                    marginTop={"0"}
                                    marginBottom={"0"}
                                  >
                                    <HBox gap={subGap}>
                                      <VBox
                                        gap={gap}
                                        mainBoxStyle={{ flexGrow: 1 }}
                                      >
                                        {solutionData.estimGenGain.cout
                                          .pouce && (
                                          <VBox>
                                            <Text
                                              text={
                                                titleSolutionData.estimGenGain
                                                  .cout.pouce
                                              }
                                              color={textColor}
                                              fontSize={
                                                subSectionFontSize + "px"
                                              }
                                              style={{
                                                textAlign: "left",
                                                display: "list-item",
                                                listStyle: "disc",
                                                listStylePosition: "inside",
                                              }}
                                            />
                                            <MarginContainer
                                              marginLeft={
                                                "calc(5 * " + globalMargin + ")"
                                              }
                                            >
                                              <VBox>
                                                <Text
                                                  text={
                                                    solutionData.estimGenGain
                                                      .cout.pouce
                                                  }
                                                  color={textColor}
                                                  fontSize={
                                                    subSectionFontSize + "px"
                                                  }
                                                  style={{
                                                    textAlign: "left",
                                                  }}
                                                />
                                              </VBox>
                                            </MarginContainer>
                                          </VBox>
                                        )}
                                        {solutionData.estimGenGain.cout
                                          .difficulte.length > 0 && (
                                          <VBox>
                                            <Text
                                              text={
                                                titleSolutionData.estimGenGain
                                                  .cout.difficulte
                                              }
                                              color={textColor}
                                              fontSize={
                                                subSectionFontSize + "px"
                                              }
                                              style={{
                                                textAlign: "left",
                                                display: "list-item",
                                                listStyle: "disc",
                                                listStylePosition: "inside",
                                              }}
                                            />
                                            <MarginContainer
                                              marginLeft={
                                                "calc(5 * " + globalMargin + ")"
                                              }
                                            >
                                              <VBox>
                                                {solutionData.estimGenGain.cout.difficulte.map(
                                                  (value, index) => {
                                                    return (
                                                      <Text
                                                        key={index}
                                                        text={value}
                                                        color={textColor}
                                                        fontSize={
                                                          subSectionFontSize +
                                                          "px"
                                                        }
                                                        style={{
                                                          textAlign: "left",
                                                          display: "list-item",
                                                          listStyle: "disc",
                                                          listStylePosition:
                                                            "outside",
                                                        }}
                                                      />
                                                    );
                                                  }
                                                )}
                                              </VBox>
                                            </MarginContainer>
                                          </VBox>
                                        )}
                                      </VBox>
                                      {solutionData.estimGenGain.cout.jauge && (
                                        <Image
                                          width="70px"
                                          height="30px"
                                          objectFit="contain"
                                          src={
                                            "/icon/jauge/cout" +
                                            solutionData.estimGenGain.cout
                                              .jauge +
                                            ".png"
                                          }
                                        />
                                      )}
                                    </HBox>
                                  </MarginContainer>
                                </VBox>
                                <VBox
                                  gap={subGap}
                                  mainBoxStyle={{
                                    width: "calc(50% - " + gap + ")",
                                  }}
                                >
                                  <ColorRect backgroundColor={textColor}>
                                    <MarginContainer
                                      margin={estimGenGainMargin}
                                      marginTop={"0"}
                                      marginBottom={"0"}
                                    >
                                      <Text
                                        text={
                                          titleSolutionData.estimGenGain.gain
                                            .title
                                        }
                                        color={negativeTextColor}
                                        fontWeight={titleFontWeight}
                                        fontSize={titleFontSize + "px"}
                                        style={{
                                          textAlign: "left",
                                        }}
                                      />
                                    </MarginContainer>
                                  </ColorRect>
                                  <MarginContainer
                                    margin={estimGenGainMargin}
                                    marginTop={"0"}
                                    marginBottom={"0"}
                                  >
                                    <HBox gap={subGap}>
                                      <VBox
                                        gap={gap}
                                        mainBoxStyle={{ flexGrow: 1 }}
                                      >
                                        {solutionData.estimGenGain.gain
                                          .gain && (
                                          <VBox>
                                            <Text
                                              text={
                                                titleSolutionData.estimGenGain
                                                  .gain.gain
                                              }
                                              color={textColor}
                                              fontSize={
                                                subSectionFontSize + "px"
                                              }
                                              style={{
                                                textAlign: "left",
                                                display: "list-item",
                                                listStyle: "disc",
                                                listStylePosition: "inside",
                                              }}
                                            />
                                            <MarginContainer
                                              marginLeft={
                                                "calc(5 * " + globalMargin + ")"
                                              }
                                            >
                                              <VBox>
                                                <Text
                                                  text={
                                                    solutionData.estimGenGain
                                                      .gain.gain
                                                  }
                                                  color={textColor}
                                                  fontSize={
                                                    subSectionFontSize + "px"
                                                  }
                                                  style={{
                                                    textAlign: "left",
                                                  }}
                                                />
                                              </VBox>
                                            </MarginContainer>
                                          </VBox>
                                        )}
                                        {solutionData.estimGenGain.gain.positif
                                          .length > 0 && (
                                          <VBox>
                                            <Text
                                              text={
                                                titleSolutionData.estimGenGain
                                                  .gain.positif
                                              }
                                              color={textColor}
                                              fontSize={
                                                subSectionFontSize + "px"
                                              }
                                              style={{
                                                textAlign: "left",
                                                display: "list-item",
                                                listStyle: "disc",
                                                listStylePosition: "inside",
                                              }}
                                            />
                                            <MarginContainer
                                              marginLeft={
                                                "calc(5 * " + globalMargin + ")"
                                              }
                                            >
                                              <VBox>
                                                {solutionData.estimGenGain.gain.positif.map(
                                                  (value, index) => {
                                                    return (
                                                      <Text
                                                        key={index}
                                                        text={value}
                                                        color={textColor}
                                                        fontSize={
                                                          subSectionFontSize +
                                                          "px"
                                                        }
                                                        style={{
                                                          textAlign: "left",
                                                          display: "list-item",
                                                          listStyle: "disc",
                                                          listStylePosition:
                                                            "outside",
                                                        }}
                                                      />
                                                    );
                                                  }
                                                )}
                                              </VBox>
                                            </MarginContainer>
                                          </VBox>
                                        )}
                                      </VBox>
                                      {solutionData.estimGenGain.gain.jauge && (
                                        <Image
                                          width="70px"
                                          height="30px"
                                          objectFit="contain"
                                          src={
                                            "/icon/jauge/gain" +
                                            solutionData.estimGenGain.gain
                                              .jauge +
                                            ".png"
                                          }
                                        />
                                      )}
                                    </HBox>
                                  </MarginContainer>
                                </VBox>
                              </HBox>
                            </VBox>

                            <MarginContainer
                              margin={lineMargin}
                              marginRight={"0"}
                              marginLeft={"0"}
                            >
                              <ColorRect
                                style={{ height: lineHeight }}
                                backgroundColor={textColor}
                              />
                            </MarginContainer>
                          </VBox>
                        )}
                        {/** ------------------------------------------------------------------------------- */}
                        {solutionData.etudeCas.length > 0 && (
                          <VBox gap={subGap}>
                            <Text
                              text={titleSolutionData.etudeCas.title}
                              color={textColor}
                              fontWeight={titleFontWeight}
                              fontSize={titleFontSize + "px"}
                              style={{
                                textAlign: "left",
                              }}
                            />
                            <VBox gap={subGap}>
                              <HBox gap={gap} justifyContent="space-around">
                                {/** Sub 1 */}
                                <VBox
                                  gap={subGap}
                                  mainBoxStyle={{
                                    width: "calc(33% - " + gap + ")",
                                  }}
                                  style={{ height: "100%" }}
                                >
                                  <ColorRect
                                    backgroundColor={orangeBackgroundColor}
                                    style={{ height: "100%" }}
                                  >
                                    <CenterContainer style={{ width: "100%" }}>
                                      <MarginContainer
                                        margin={estimGenGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <Text
                                          text={titleSolutionData.etudeCas.sub1}
                                          color={negativeTextColor}
                                          fontWeight={titleFontWeight}
                                          fontSize={titleFontSize + "px"}
                                          style={{
                                            textAlign: "left",
                                          }}
                                        />
                                      </MarginContainer>
                                    </CenterContainer>
                                  </ColorRect>
                                </VBox>
                                {/** Sub 2 */}
                                <VBox
                                  gap={subGap}
                                  mainBoxStyle={{
                                    width: "calc(33% - " + gap + ")",
                                  }}
                                  style={{ height: "100%" }}
                                >
                                  <ColorRect
                                    backgroundColor={badBackgroundColor}
                                    style={{ height: "100%" }}
                                  >
                                    <CenterContainer style={{ width: "100%" }}>
                                      <MarginContainer
                                        margin={estimGenGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <Text
                                          text={titleSolutionData.etudeCas.sub2}
                                          color={negativeTextColor}
                                          fontWeight={titleFontWeight}
                                          fontSize={titleFontSize + "px"}
                                          style={{
                                            textAlign: "left",
                                          }}
                                        />
                                      </MarginContainer>
                                    </CenterContainer>
                                  </ColorRect>
                                </VBox>
                                {/** Sub 3 */}
                                <VBox
                                  gap={subGap}
                                  mainBoxStyle={{
                                    width: "calc(33% - " + gap + ")",
                                  }}
                                  style={{ height: "100%" }}
                                >
                                  <ColorRect
                                    backgroundColor={textColor}
                                    style={{ height: "100%" }}
                                  >
                                    <CenterContainer style={{ width: "100%" }}>
                                      <MarginContainer
                                        margin={estimGenGainMargin}
                                        marginTop={"0"}
                                        marginBottom={"0"}
                                      >
                                        <Text
                                          text={titleSolutionData.etudeCas.sub3}
                                          color={negativeTextColor}
                                          fontWeight={titleFontWeight}
                                          fontSize={titleFontSize + "px"}
                                          style={{
                                            textAlign: "left",
                                          }}
                                        />
                                      </MarginContainer>
                                    </CenterContainer>
                                  </ColorRect>
                                </VBox>
                              </HBox>
                              <VBox gap={gap}>
                                {solutionData.etudeCas.map((ec, index) => {
                                  return (
                                    <VBox gap="10px" key={index}>
                                      <HBox
                                        gap={gap}
                                        justifyContent="space-around"
                                      >
                                        {/** Sub 1 */}
                                        <VBox
                                          gap={"calc(" + subGap + " / 2)"}
                                          justifyContent="start"
                                          mainBoxStyle={{
                                            width: "calc(33% - " + gap + ")",
                                          }}
                                        >
                                          <Text
                                            text={ec.sub1}
                                            color={textColor}
                                            fontSize={subSectionFontSize + "px"}
                                            style={{
                                              textAlign: "left",
                                            }}
                                          />
                                        </VBox>
                                        {/** Sub 2 */}
                                        <VBox
                                          gap={"calc(" + subGap + " / 2)"}
                                          justifyContent="start"
                                          mainBoxStyle={{
                                            width: "calc(33% - " + gap + ")",
                                          }}
                                        >
                                          {ec.sub2 &&
                                            ec.sub2.map((value, index) => {
                                              return (
                                                <Text
                                                  key={index}
                                                  text={value}
                                                  color={textColor}
                                                  fontSize={
                                                    subSectionFontSize + "px"
                                                  }
                                                  style={{
                                                    textAlign: "left",
                                                  }}
                                                />
                                              );
                                            })}
                                        </VBox>
                                        {/** Sub 3 */}
                                        <VBox
                                          gap={"calc(" + subGap + " / 2)"}
                                          justifyContent="start"
                                          mainBoxStyle={{
                                            width: "calc(33% - " + gap + ")",
                                          }}
                                        >
                                          {ec.sub3 &&
                                            ec.sub3.map((value, index) => {
                                              return (
                                                <Text
                                                  key={index}
                                                  text={value}
                                                  color={textColor}
                                                  fontSize={
                                                    subSectionFontSize + "px"
                                                  }
                                                  style={{
                                                    textAlign: "left",
                                                  }}
                                                />
                                              );
                                            })}
                                        </VBox>
                                      </HBox>
                                      <CenterContainer
                                        style={{
                                          width: "100%",
                                          display:
                                            index ===
                                            solutionData.etudeCas.length - 1
                                              ? "none"
                                              : "",
                                        }}
                                      >
                                        <ColorRect
                                          backgroundColor={textColor}
                                          style={{ height: "1px" }}
                                        />
                                      </CenterContainer>
                                    </VBox>
                                  );
                                })}
                              </VBox>
                            </VBox>
                          </VBox>
                        )}
                        {/** ------------------------------------------------------------------------------- */}
                      </VBox>
                    </MarginContainer>
                  </div>
                </div>
              </MarginContainer>
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
        widthParent="10px"
      />
    </HBox>
  );
};

export default SolutionDetails;
