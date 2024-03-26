import { ColorRect, MarginContainer, Text } from "@liro_u/react-components";
import React from "react";

const Tableau = ({
  tab,
  color,
  titleFontWeight,
  titleFontSize,
  subSectionFontSize = "15",
  border = "solid 0px var(--dark-primary)",
  marginCase = "10px",
  headerBackgroundColor = "var(--dark-primary)",
  evenBackgroundColor = "var(--primary-pastel)",
  oddBackgroundColor = "var(--dark-primary-pastel)",
  headerTextColor = "var(--light-color)",
  borderSpacing = "0",
}) => {
  const cssBorder = {
    borderLeft: border,
    borderRight: border,
  };

  return (
    <table style={{ ...cssBorder, borderCollapse: "collapse", borderSpacing }}>
      {tab.map((line, index1) => {
        return (
          <tr
            key={index1}
            style={{ ...cssBorder, borderCollapse: "collapse", borderSpacing }}
          >
            {line.map((col, index2) => {
              return (
                <td
                  key={index2}
                  style={{
                    ...cssBorder,
                    borderCollapse: "collapse",
                    borderSpacing,
                  }}
                >
                  <ColorRect
                    backgroundColor={
                      index1 === 0
                        ? headerBackgroundColor
                        : index1 % 2 === 0
                        ? evenBackgroundColor
                        : oddBackgroundColor
                    }
                  >
                    <MarginContainer margin={marginCase}>
                      <Text
                        text={col}
                        fontWeight={index1 === 0 ? titleFontWeight : ""}
                        fontSize={subSectionFontSize + "px"}
                        color={index1 === 0 ? headerTextColor : color}
                      />
                    </MarginContainer>
                  </ColorRect>
                </td>
              );
            })}
          </tr>
        );
      })}
    </table>
  );
};

export default Tableau;
