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

const SolutionFinder = ({
  callBack = (solutions) => {
    console.log(solutions);
  },
}) => {
  // content customisation variable
  const section2Text = "Description *";
  const section1Text = "Secteur d'activité";
  const subSection1Text = "Sous-secteur *";
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

  const subSectionBoxShadow = "0px 4px 4px 0px #00000040";

  // css auto variable
  const subSectionVerticalMargin = titleFontSize - subSectionFontSize;
  const subSectionHorizontalMargin = subSectionFontSize;

  // react update variable
  const [description, setDescription] = useState("");
  const [sectors, setSectors] = useState({});
  const [mainCategorie, setMainCategorie] = useState(null);
  const [subCategorie, setSubCategorie] = useState(null);
  const [isSubSectionError, setIsSubSectionError] = useState(false);
  const [isDescriptionError, setIsDescriptionError] = useState(false);

  useEffect(() => {
    const getAllCategories = async () => {
      const response = await fetch(
        process.env.REACT_APP_PROXY + "/sec/get_all_sector"
      );

      const json = await response.json();

      if (response.ok) {
        const data = json.sectors;
        setSectors(data);
      } else {
      }
    };
    getAllCategories();
  }, []);

  // API call
  const askAPIForSolutions = async () => {
    if (!subCategorie) {
      setIsSubSectionError(true);
    }
    if (!description || description === "") {
      setIsDescriptionError(true);
    }

    if (description && subCategorie && description !== "") {
      const response = await fetch(
        process.env.REACT_APP_PROXY + "/sol/best_solutions",
        {
          method: "POST",
          body: JSON.stringify({ secteur_activite: subCategorie, description }),
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
  };

  const selectMainCategorie = (value) => {
    setMainCategorie(value);
    setSubCategorie(null);
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
            <CustomSelect
              options={Object.keys(sectors)}
              backgroundColor={backgroundColor}
              borderRadius={subSectionBorderRadius}
              boxShadow={subSectionBoxShadow}
              width={subSectionPercentage}
              horizontalMargin={subSectionHorizontalMargin}
              verticalMargin={subSectionVerticalMargin}
              textColor={textColor}
              fontSize={subSectionFontSize}
              HGap={"calc(" + gap + " / 2)"}
              currentValue={mainCategorie}
              selectCallback={selectMainCategorie}
            />
          </HBox>
          <HBox justifyContent="space-between">
            <Text
              text={subSection1Text}
              color={textColor}
              fontWeight={titleFontWeight}
              fontSize={titleFontSize + "px"}
            />
            <CustomSelect
              options={
                mainCategorie ? [mainCategorie, ...sectors[mainCategorie]] : []
              }
              backgroundColor={backgroundColor}
              borderRadius={subSectionBorderRadius}
              boxShadow={subSectionBoxShadow}
              width={subSectionPercentage}
              horizontalMargin={subSectionHorizontalMargin}
              verticalMargin={subSectionVerticalMargin}
              textColor={isSubSectionError ? "red" : textColor}
              fontSize={subSectionFontSize}
              HGap={"calc(" + gap + " / 2)"}
              currentValue={subCategorie}
              selectCallback={selectSubCategorie}
              style={isSubSectionError ? { border: "solid 1px red" } : {}}
            />
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
                color={isDescriptionError ? "red" : textColor}
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
                  isDescriptionError ? { border: "solid 1px red" } : {}
                }
              />
            </ColorRect>
          </HBox>
          <HBox justifyContent="right">
            <CustomButton
              fontSize={subSectionFontSize}
              horizontalMargin={subSectionHorizontalMargin}
              verticalMargin={subSectionVerticalMargin}
              boxShadow={subSectionBoxShadow}
              onClick={askAPIForSolutions}
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
