import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useState } from "react";
import CustomButton from "./input/CustomButton";

const SubSolutionDisplay = ({
  callBack = (solution) => {
    console.log(solution);
  },
  textColor = "var(--dark-primary)",
  margin = "20px",
  fontSize = 15,
  fontWeight = "bold",
  gap = "20px",
  percentageSplit = [10, 30, 20, 10, 10, 10, 10],
  solution,
  noData = "-",
}) => {
  const verticalMargin = "calc(" + margin + " / 3)";
  const lorem =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate  velit esse cillum dolore eu fugiat nulla pariatur.";

  const testSolutionData = {
    numSolution: "54",
    titleSolution: "Moteur a haut rendement",
    technologie: "Moteur",
    definition: lorem,
    application: lorem,
    bilanEnergie: lorem,
    estimPersoGain: {
      degConf: 15,
      euro: "1 832 056 €/an",
      gwh: "53 GWh/an",
      co2: "100T",
      gainReel: "1 832 066 €",
      retourInv: "2,5 ans",
      coutFinance: "5 718 920 €",
    },
    estimGenGain: {
      cout: {
        pouce:
          "de 20 à 30 % de surcoût pour les moteurs d'une puissance supérieure à 20 kW  [Source : Top motors].",
        difficulte: [
          "Sauf changement radical de technologie, les moteurs   sont de même taille et ont une augmentation de poids d’environ 15 %.",
        ],
      },
      gain: {
        gain: "de 2 à 10 % d'augmentation du rendement selon les puissance par rapport à la norme IE1  [Source : Top motors].",
        positif: [
          "Anticipation des contraintes légales à venir.",
          "Gain sur la durée de vie du moteur.",
        ],
      },
    },
    etudeCas: [
      {
        sub1: "14. Fruits et légumes / France",
        sub2: ["Coûts 12 000 €", "Difficulté : Long a mettre en oeuvre"],
        sub3: [
          "Gains Financier : 6 635 €/an",
          "Economie d'énergie : 144 MWh/an",
          "Economies d'électricité",
        ],
      },
      {
        sub1: "134. Ciment / Phillipine",
      },
      {
        sub1: "791. Enseignement / Canada",
        sub2: ["Ajout de moteurs pour optimiser la ventillation"],
      },
    ],
  };

  const [isLoading, setIsLoading] = useState(false);

  const askAPIForSolutionDetails = async () => {
    setIsLoading(true);

    const response = await fetch(
      process.env.REACT_APP_PROXY +
        "/sol/data_solution/" +
        solution.num +
        "/" +
        solution.codeSector
    );

    const json = await response.json();

    if (response.ok) {
      const data = testSolutionData; // data

      callBack(data);
    } else {
      callBack(testSolutionData);
    }

    setIsLoading(false);
  };

  return (
    <MarginContainer
      margin={verticalMargin}
      marginLeft={margin}
      marginRight={margin}
    >
      <VBox gap={"calc( " + gap + " / 4)"}>
        <HBox gap={gap}>
          <Text
            text={solution.num ? solution.num : noData}
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[0] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <Text
            text={solution.titre ? solution.titre : noData}
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[1] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <Text
            text={
              "Basé sur " +
              solution.estimPersoGain.number_of_based_solutions +
              " études"
            }
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[2] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <Text
            text={
              solution.estimPersoGain.average_financial_gain
                ? Math.round(solution.estimPersoGain.average_financial_gain) +
                  " €" +
                  (solution.estimPersoGain.nom_periode_economie
                    ? solution.estimPersoGain.nom_periode_economie
                    : "")
                : noData
            }
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[3] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <Text
            text={
              solution.estimPersoCout.average_cout
                ? Math.round(solution.estimPersoCout.average_cout) + " €"
                : noData
            }
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[4] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <Text
            text={
              solution.estimPersoGain.average_energy_gain
                ? Math.round(solution.estimPersoGain.average_energy_gain) +
                  " " +
                  solution.estimPersoGain.nom_unite_energie
                  ? solution.estimPersoGain.nom_unite_energie +
                    (solution.estimPersoGain.nom_periode_energie
                      ? solution.estimPersoGain.nom_periode_energie
                      : "")
                  : ""
                : noData
            }
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[5] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <Text
            text={
              solution.estimPersoGain.average_ges_gain
                ? Math.round(solution.estimPersoGain.average_ges_gain) +
                  " tCO2eq"
                : noData
            }
            color={textColor}
            fontSize={fontSize}
            fontWeight={fontWeight}
            style={{
              width: "calc(" + percentageSplit[6] + "% - " + gap + ")",
              textAlign: "left",
            }}
          />
          <CustomButton
            fontSize={fontSize}
            isDisable={isLoading}
            buttonWidth={"calc(" + percentageSplit[7] + "% - " + gap + ")"}
            text="Détails"
            onClick={askAPIForSolutionDetails}
          />
        </HBox>
        <ColorRect backgroundColor={textColor} style={{ height: "0.5px" }} />
      </VBox>
    </MarginContainer>
  );
};

export default SubSolutionDisplay;
