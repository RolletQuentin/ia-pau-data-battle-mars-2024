import {
  ColorRect,
  HBox,
  MarginContainer,
  Text,
  VBox,
} from "@liro_u/react-components";
import React, { useState } from "react";
import CustomButton from "./input/CustomButton";
import {
  bigNumber2String,
  cropperFloat,
  getCurrentCodeLangue,
} from "../usefull";

import { useTranslation } from "react-i18next";

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
  const { t } = useTranslation();

  const verticalMargin = "calc(" + margin + " / 3)";

  const [isLoading, setIsLoading] = useState(false);

  const createSub2 = (sub2Data) => {
    const sub2 = [];

    if (sub2Data.cout_reel) {
      sub2.push(
        t("solutionDetail.builder.couts") +
          bigNumber2String(sub2Data.cout_reel) +
          " " +
          (sub2Data.monnaie && sub2Data.monnaie.short_monnaie
            ? sub2Data.monnaie.short_monnaie
            : "€")
      );
    }

    if (sub2Data.code_difficulte) {
      sub2.push(
        t("solutionDetail.builder.difficulte") + sub2Data.code_difficulte
      );
    }

    if (sub2Data.text) {
      sub2.push(sub2Data.text);
    }

    return sub2;
  };

  const createSub3 = (sub3Data) => {
    const sub3 = [];

    if (sub3Data.gain_financier) {
      sub3.push(
        t("solutionDetail.builder.gainF") +
          bigNumber2String(sub3Data.gain_financier) +
          " " +
          (sub3Data.monnaie && sub3Data.monnaie.short_monnaie
            ? sub3Data.monnaie.short_monnaie
            : "€") +
          (sub3Data.nom_periode_economie ? sub3Data.nom_periode_economie : "")
      );
    }

    if (sub3Data.tri_reel) {
      sub3.push(
        t("solutionDetail.builder.TRI") +
          cropperFloat(sub3Data.tri_reel) +
          t("solutionDetail.builder.ans")
      );
    }

    if (sub3Data.gain_energie) {
      sub3.push(
        t("solutionDetail.builder.ecoE") +
          bigNumber2String(sub3Data.gain_energie) +
          " " +
          (sub3Data.nom_unite_energie ? sub3Data.nom_unite_energie : "") +
          (sub3Data.nom_periode_energie ? sub3Data.nom_periode_energie : "")
      );
    }

    if (sub3Data.gain_ges) {
      sub3.push(
        t("solutionDetail.builder.eGESdodge") +
          bigNumber2String(sub3Data.gain_ges) +
          t("solutionDetail.builder.tCO2eqAn")
      );
    }

    if (sub3Data.gain_reel) {
      sub3.push(
        t("solutionDetail.builder.gainReel") +
          bigNumber2String(sub3Data.gain_reel) +
          " €"
      );
    }

    if (sub3Data.text) {
      sub3.push(sub3Data.text);
    }

    return sub3;
  };

  const createEtudeCas = (givenEtudeCas) => {
    const etudeCas = [];

    givenEtudeCas.forEach((ec, index) => {
      etudeCas[index] = {
        sub1:
          ec.numRex +
          ". " +
          (ec.sector ? ec.sector : "") +
          (ec.sector && ec.pays ? " / " : "") +
          (ec.pays ? ec.pays : "") +
          (ec.pays && ec.date ? " / " : "") +
          (!ec.pays && ec.sector && ec.date ? " / " : "") +
          (ec.date ? ec.date : ""),
        sub2: ec.cout ? createSub2(ec.cout) : [],
        sub3: ec.gain ? createSub3(ec.gain) : [],
      };
    });

    return etudeCas;
  };

  const askAPIForSolutionDetails = async () => {
    setIsLoading(true);

    const response = await fetch(
      process.env.REACT_APP_PROXY +
        "/sol/data_solution/" +
        solution.num +
        "/" +
        solution.codeSector +
        "/" +
        getCurrentCodeLangue()
    );

    const json = await response.json();

    if (response.ok) {
      const data = {
        numSolution: json.numSolution,
        titleSolution: json.titre,
        technologie: json.technologie,
        definition: json.definition,
        application: json.application,
        bilanEnergie: json.bilanEnergie,
        estimPersoGain: {
          degConf: json.estimPerso.estimPersoGain.number_of_based_solutions,
          euro: json.estimPerso.estimPersoGain.average_financial_gain
            ? bigNumber2String(
                json.estimPerso.estimPersoGain.average_financial_gain
              ) +
              " €" +
              (json.estimPerso.estimPersoGain.nom_periode_economie
                ? json.estimPerso.estimPersoGain.nom_periode_economie
                : "")
            : noData,
          gwh: json.estimPerso.estimPersoGain.average_energy_gain
            ? bigNumber2String(
                json.estimPerso.estimPersoGain.average_energy_gain
              ) +
              " " +
              (json.estimPerso.estimPersoGain.nom_unite_energie
                ? json.estimPerso.estimPersoGain.nom_unite_energie +
                  (json.estimPerso.estimPersoGain.nom_periode_energie
                    ? json.estimPerso.estimPersoGain.nom_periode_energie
                    : "")
                : "")
            : noData,
          co2: json.estimPerso.estimPersoGain.average_ges_gain
            ? bigNumber2String(
                json.estimPerso.estimPersoGain.average_ges_gain
              ) + t("solutionDetail.builder.tCO2eq")
            : noData,
          gainReel: json.estimPerso.estimPersoGain.average_real_gain
            ? bigNumber2String(
                json.estimPerso.estimPersoGain.average_real_gain
              ) + " €"
            : noData,
          retourInv: json.estimPerso.estimPersoGain.average_real_tri
            ? cropperFloat(json.estimPerso.estimPersoGain.average_real_tri) +
              t("solutionDetail.builder.ans")
            : noData,
          coutFinance: json.estimPerso.estimPersoCout.average_cout
            ? bigNumber2String(json.estimPerso.estimPersoCout.average_cout) +
              " €"
            : noData,
        },
        estimGenGain: {
          cout: {
            jauge: json.estimGen.cout.jaugeCout,
            pouce: json.estimGen.cout.pouce,
            difficulte: json.estimGen.cout.difficulte,
          },
          gain: {
            jauge: json.estimGen.gain.jaugeGain,
            gain: json.estimGen.gain.gain,
            positif: json.estimGen.gain.positif,
          },
        },
        etudeCas: createEtudeCas(json.listRex),
      };

      callBack(data);
    } else {
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
              t("based_on") +
              " " +
              solution.estimPersoGain.number_of_based_solutions +
              " " +
              t("studies")
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
                ? bigNumber2String(
                    solution.estimPersoGain.average_financial_gain
                  ) +
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
                ? bigNumber2String(solution.estimPersoCout.average_cout) + " €"
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
                ? bigNumber2String(
                    solution.estimPersoGain.average_energy_gain
                  ) +
                  " " +
                  (solution.estimPersoGain.nom_unite_energie
                    ? solution.estimPersoGain.nom_unite_energie +
                      (solution.estimPersoGain.nom_periode_energie
                        ? solution.estimPersoGain.nom_periode_energie
                        : "")
                    : "")
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
                ? bigNumber2String(solution.estimPersoGain.average_ges_gain) +
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
            text={t("buttons.details")}
            onClick={askAPIForSolutionDetails}
          />
        </HBox>
        <ColorRect backgroundColor={textColor} style={{ height: "1px" }} />
      </VBox>
    </MarginContainer>
  );
};

export default SubSolutionDisplay;
