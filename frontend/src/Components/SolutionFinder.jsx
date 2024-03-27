import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useEffect, useState } from "react";
import TextArea from "./input/TextArea";
import CustomButton from "./input/CustomButton";
import CustomSelect from "./input/CustomSelect";

import { useTranslation } from "react-i18next";
import { getCurrentCodeLangue } from "../usefull";
import i18n from "../i18n";

const SolutionFinder = ({
  callBack = (solutions) => {
    console.log(solutions);
  },
  maxChar = 2048,
  // css customisation variable
  backgroundColor = "#ededed",
  backgroundColorAlpha = "e3",
  backgroundBlur = "blur(20px)",
  titleFontSize = 20,
  textColor = "var(--dark-primary)",
  subSectionFontSize = 15,
  globalMargin = "50px",
  titleFontWeight = "bold",
  borderRadius = "30px",
  gap = "20px",
  subSectionBoxShadow = "0px 4px 4px 0px #00000040",
  subSectionBorderRadius = "20px",
  subSectionPercentage = "70%",
  errorColor = "var(--error)",
  // content customisation variable
  section2Text = "Description *",
  section1Text = "Secteur d'activité *",
  subSection1Text = "Sous-secteur *",
  validateButtonText = "Mes solutions",
  mainSectionAsSubSection = "Autres",
  descriptionTextPlaceholder = "Exemple : Mettre en transparance un exemple bien détaillé de ce que l’user doit écrire dans cette section. Comme ça on augmente les chances qu’il écrive pas n’importe quoi.",
}) => {
  const { t } = useTranslation();

  // css auto variable
  const subSectionVerticalMargin = titleFontSize - subSectionFontSize;
  const subSectionHorizontalMargin = subSectionFontSize;

  // react update variable
  const [description, setDescription] = useState("");
  const [sectors, setSectors] = useState({});
  const [mainCategorie, setMainCategorie] = useState(null);
  const [subCategorie, setSubCategorie] = useState(null);
  const [isMainSectionError, setIsMainSectionError] = useState(false);
  const [isSubSectionError, setIsSubSectionError] = useState(false);
  const [isDescriptionError, setIsDescriptionError] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    const getAllCategories = async () => {
      const response = await fetch(
        process.env.REACT_APP_PROXY +
          "/sec/get_all_sector/" +
          getCurrentCodeLangue()
      );

      const json = await response.json();

      if (response.ok) {
        const data = json.sectors;
        setSectors(data);
      } else {
      }
    };
    getAllCategories();

    const languageChangeHandler = () => {
      setMainCategorie(null);
      setSubCategorie(null);
      getAllCategories();
    };

    i18n.on("languageChanged", languageChangeHandler);

    return () => i18n.off("languageChanged", languageChangeHandler);
  }, []);

  // API call
  const askAPIForSolutions = async () => {
    setIsLoading(true);

    if (!mainCategorie) {
      setIsMainSectionError(true);
    } else if (!subCategorie) {
      setIsSubSectionError(true);
    }
    if (!description || description === "" || description.length > maxChar) {
      setIsDescriptionError(true);
    }

    if (
      mainCategorie &&
      description &&
      subCategorie &&
      description !== "" &&
      description.length <= maxChar
    ) {
      const response = await fetch(
        process.env.REACT_APP_PROXY + "/sol/best_solutions",
        {
          method: "POST",
          body: JSON.stringify({
            secteur_activite:
              subCategorie === mainSectionAsSubSection
                ? mainCategorie
                : subCategorie,
            description,
            code_langue: getCurrentCodeLangue(),
          }),
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      const json = await response.json();

      if (response.ok) {
        const data = json;

        callBack(data);
      } else {
      }
    }

    setIsLoading(false);
  };

  const selectMainCategorie = (value) => {
    setMainCategorie(value);
    setSubCategorie(null);
    if (isMainSectionError) {
      setIsMainSectionError(false);
    }
  };

  const selectSubCategorie = (value) => {
    setSubCategorie(value);
    if (isSubSectionError) {
      setIsSubSectionError(false);
    }
  };

  const descriptionChanged = (value) => {
    setDescription(value);
    if (isDescriptionError) {
      setIsDescriptionError(false);
    }
  };

  return (
    <ColorRect
      backgroundColor={backgroundColor + backgroundColorAlpha}
      style={{
        borderRadius,
        width: "50vw",
        boxShadow: subSectionBoxShadow,
        backdropFilter: backgroundBlur,
      }}
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
            <CustomSelect
              options={Object.keys(sectors)}
              backgroundColor={backgroundColor}
              borderRadius={subSectionBorderRadius}
              boxShadow={subSectionBoxShadow}
              width={subSectionPercentage}
              horizontalMargin={subSectionHorizontalMargin}
              verticalMargin={subSectionVerticalMargin}
              textColor={isMainSectionError ? errorColor : textColor}
              fontSize={subSectionFontSize}
              HGap={"calc(" + gap + " / 2)"}
              currentValue={mainCategorie}
              selectCallback={selectMainCategorie}
              style={
                isMainSectionError ? { border: "solid 2px " + errorColor } : {}
              }
              noOptionsError={t("solutionFinder.noOptionsError")}
              noOptionsSelectedError={t(
                "solutionFinder.noOptionsSelectedSectorError"
              )}
            />
          </HBox>
          <HBox
            justifyContent="space-between"
            style={{
              maxHeight: mainCategorie ? "200px" : "0",
              overflow: mainCategorie ? "" : "hidden",
              transition: "max-height 1s",
            }}
          >
            <Text
              text={subSection1Text}
              color={textColor}
              fontWeight={titleFontWeight}
              fontSize={titleFontSize + "px"}
            />
            <CustomSelect
              options={
                mainCategorie
                  ? [...sectors[mainCategorie], mainSectionAsSubSection]
                  : []
              }
              backgroundColor={backgroundColor}
              borderRadius={subSectionBorderRadius}
              boxShadow={subSectionBoxShadow}
              width={subSectionPercentage}
              horizontalMargin={subSectionHorizontalMargin}
              verticalMargin={subSectionVerticalMargin}
              textColor={isSubSectionError ? errorColor : textColor}
              fontSize={subSectionFontSize}
              HGap={"calc(" + gap + " / 2)"}
              currentValue={subCategorie}
              selectCallback={selectSubCategorie}
              style={
                isSubSectionError ? { border: "solid 2px " + errorColor } : {}
              }
              noOptionsError={t("solutionFinder.noOptionsError")}
              noOptionsSelectedError={t(
                "solutionFinder.noOptionsSelectedSubSectorError"
              )}
            />
          </HBox>
          <HBox justifyContent="space-between">
            <VBox justifyContent="start">
              <Text
                text={section2Text}
                color={textColor}
                fontWeight={titleFontWeight}
                fontSize={titleFontSize + "px"}
              />
              <Text
                text={"(" + description.length + "/" + maxChar + " char)"}
                fontSize={subSectionFontSize}
                color={
                  description.length <= maxChar ? textColor : "var(--error)"
                }
                style={{ textAlign: "start" }}
              />
            </VBox>
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
                placeholder={
                  descriptionTextPlaceholder[
                    Math.floor(
                      Math.random() * descriptionTextPlaceholder.length
                    )
                  ]
                }
                color={isDescriptionError ? errorColor : textColor}
                setValue={descriptionChanged}
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
                basicStyle={
                  isDescriptionError
                    ? { border: "solid 2px " + errorColor }
                    : {}
                }
              />
            </ColorRect>
          </HBox>
          <HBox justifyContent="right">
            <CustomButton
              isDisable={isLoading}
              fontSize={subSectionFontSize}
              horizontalMargin={subSectionHorizontalMargin}
              verticalMargin={subSectionVerticalMargin}
              boxShadow={subSectionBoxShadow}
              onClick={isLoading ? () => {} : askAPIForSolutions}
              borderRadius={subSectionBorderRadius}
              text={validateButtonText}
            />
          </HBox>
        </VBox>
      </MarginContainer>
    </ColorRect>
  );
};

export default SolutionFinder;
