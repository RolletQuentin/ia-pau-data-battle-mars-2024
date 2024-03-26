import React, { useEffect, useRef, useState } from "react";
import { useTranslation } from "react-i18next";
import i18n from "../i18n";
import { CenterContainer, HBox, Text, VBox } from "@liro_u/react-components";
import LanguageButton from "./subComponents/LanguageButton";

const LanguageSelector = ({
  style,
  borderColor = "var(--primary)",
  backgroundColor = "var(--dark-primary)",
  textColor = "var(--light-color)",
}) => {
  const { t } = useTranslation();
  const containerRef = useRef(null);

  const [isHover, setIsHover] = useState(false);
  const [isFocus, setIsFocus] = useState(false);

  const handleHover = (hoverBool) => {
    setIsHover(hoverBool);
  };

  const toggleFocus = () => {
    setIsFocus(!isFocus);
  };

  const handleGlobalClick = (event) => {
    if (containerRef.current && !containerRef.current.contains(event.target)) {
      setIsFocus(false);
    }
  };

  useEffect(() => {
    window.addEventListener("click", handleGlobalClick);
    return () => {
      window.removeEventListener("click", handleGlobalClick);
    };
  }, []);

  return (
    <div style={style} ref={containerRef}>
      <CenterContainer style={{ position: "relative" }}>
        <HBox
          style={{
            padding: "10px",
            border: "3px solid",
            borderColor,
            backgroundColor,
            borderRadius: "100px",
            overflow: "hidden",
            cursor: "pointer",
          }}
          onMouseEnter={() => handleHover(true)}
          onMouseLeave={() => handleHover(false)}
          tabIndex={0}
          onClick={toggleFocus}
        >
          <span
            className="material-symbols-outlined"
            style={{
              fontSize: "40px",
              margin: "auto",
              color: textColor,
            }}
          >
            public
          </span>
          <HBox
            style={{
              width: isHover || isFocus ? "200px" : "0",
              transition: "width 0.5s",
            }}
          >
            <Text
              fontSize="20px"
              text={t("language." + i18n.language)}
              color={textColor}
              style={{
                margin: "auto",
                width: "150px",
                textAlign: "left",
                paddingLeft: "30px",
              }}
            />
            <span
              className="material-symbols-outlined"
              style={{ fontSize: "40px", margin: "auto", color: textColor }}
            >
              {isFocus ? "arrow_drop_up" : "arrow_drop_down"}
            </span>
          </HBox>
        </HBox>
        {isFocus && (
          <VBox
            mainBoxStyle={{
              top: "auto",
              bottom: "calc(100% + 4px)",
              left: "50%",
              transform: "translateX(-50%)",
              position: "absolute",
              backgroundColor: "#222",
              padding: "10px 20px",
              minWidth: "100%",
            }}
          >
            <LanguageButton lg="fr" />
            <LanguageButton lg="en" />
            <LanguageButton lg="es" />
          </VBox>
        )}
      </CenterContainer>
    </div>
  );
};

export default LanguageSelector;
