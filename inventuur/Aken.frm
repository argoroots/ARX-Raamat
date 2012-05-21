VERSION 5.00
Begin VB.Form Aken 
   Caption         =   "Form1"
   ClientHeight    =   6675
   ClientLeft      =   60
   ClientTop       =   375
   ClientWidth     =   14910
   DrawMode        =   1  'Blackness
   BeginProperty Font 
      Name            =   "Verdana"
      Size            =   9
      Charset         =   186
      Weight          =   400
      Underline       =   0   'False
      Italic          =   0   'False
      Strikethrough   =   0   'False
   EndProperty
   Icon            =   "Aken.frx":0000
   LinkTopic       =   "Form1"
   ScaleHeight     =   6675
   ScaleWidth      =   14910
   StartUpPosition =   3  'Windows Default
   Begin VB.TextBox Text1 
      Appearance      =   0  'Flat
      BackColor       =   &H8000000F&
      BorderStyle     =   0  'None
      Height          =   1170
      Left            =   105
      Locked          =   -1  'True
      MultiLine       =   -1  'True
      TabIndex        =   9
      TabStop         =   0   'False
      Text            =   "Aken.frx":2964A
      Top             =   105
      Width           =   12615
   End
   Begin VB.CommandButton btnPrint 
      Caption         =   "Salvesta aruanne"
      Enabled         =   0   'False
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   9
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   435
      Left            =   12810
      TabIndex        =   5
      Top             =   105
      Width           =   2010
   End
   Begin VB.ComboBox cmbLiik 
      Height          =   330
      IntegralHeight  =   0   'False
      ItemData        =   "Aken.frx":2970C
      Left            =   105
      List            =   "Aken.frx":2970E
      Style           =   2  'Dropdown List
      TabIndex        =   4
      Top             =   1680
      Width           =   1590
   End
   Begin VB.ListBox lstSelected 
      Height          =   4665
      IntegralHeight  =   0   'False
      ItemData        =   "Aken.frx":29710
      Left            =   7875
      List            =   "Aken.frx":29712
      TabIndex        =   3
      Top             =   1680
      Width           =   6945
   End
   Begin VB.CommandButton btnSearch 
      Caption         =   "Otsi"
      Default         =   -1  'True
      Height          =   330
      Left            =   6405
      TabIndex        =   2
      Top             =   1680
      Width           =   750
   End
   Begin VB.TextBox txtSearch 
      Height          =   330
      Left            =   1785
      TabIndex        =   1
      Top             =   1680
      Width           =   4530
   End
   Begin VB.ListBox lstMedia 
      Height          =   3690
      IntegralHeight  =   0   'False
      ItemData        =   "Aken.frx":29714
      Left            =   105
      List            =   "Aken.frx":29716
      TabIndex        =   0
      Top             =   2100
      Width           =   6420
   End
   Begin VB.Frame frmButtons 
      Appearance      =   0  'Flat
      BorderStyle     =   0  'None
      Caption         =   "Frame1"
      ForeColor       =   &H80000008&
      Height          =   1380
      Left            =   6825
      TabIndex        =   6
      Top             =   3150
      Width           =   750
      Begin VB.CommandButton btnSelect 
         Appearance      =   0  'Flat
         Caption         =   ">"
         BeginProperty Font 
            Name            =   "Verdana"
            Size            =   8.25
            Charset         =   186
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   540
         Left            =   105
         TabIndex        =   8
         Top             =   105
         Width           =   540
      End
      Begin VB.CommandButton btnDeselect 
         Caption         =   "<"
         BeginProperty Font 
            Name            =   "Verdana"
            Size            =   8.25
            Charset         =   186
            Weight          =   700
            Underline       =   0   'False
            Italic          =   0   'False
            Strikethrough   =   0   'False
         EndProperty
         Height          =   540
         Left            =   105
         TabIndex        =   7
         Top             =   735
         Width           =   540
      End
   End
   Begin VB.Label lblSelected 
      AutoSize        =   -1  'True
      Caption         =   "Teavikud mis on (inventuuri hetkel) raamatukogus olemas:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   9
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   210
      Left            =   7875
      TabIndex        =   11
      Top             =   1365
      Width           =   5820
   End
   Begin VB.Label Label1 
      AutoSize        =   -1  'True
      Caption         =   "Raamatukogu kataloog:"
      BeginProperty Font 
         Name            =   "Verdana"
         Size            =   9
         Charset         =   186
         Weight          =   700
         Underline       =   0   'False
         Italic          =   0   'False
         Strikethrough   =   0   'False
      EndProperty
      Height          =   210
      Left            =   105
      TabIndex        =   10
      Top             =   1365
      Width           =   2340
   End
End
Attribute VB_Name = "Aken"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = True
Attribute VB_Exposed = False
Option Explicit

Dim gConnect As ADODB.Connection
Dim gRS As ADODB.Recordset

Private Sub Form_Load()
    On Error GoTo Viga
    Dim mySQL As String
    Dim myName As String
    Dim myFile As String
    Dim a As String
    
Algus:
    
    Open App.Path & "\Raamat.ini" For Input As #1
    Do Until EOF(1)
        Line Input #1, a
        If Left(a, 4) = "MDB=" Then myFile = Mid(a, 5)
    Loop
    Close #1
    
    If LenB(myFile) = 0 Then
        End
    Else
        Set gConnect = New ADODB.Connection
        Set gRS = New ADODB.Recordset
        gConnect.Open "PROVIDER=Microsoft.Jet.OLEDB.4.0;Data Source=""" & myFile & """;"
    End If
    
    Me.Caption = App.ProductName & " - " & App.Major & "." & App.Minor & "." & App.Revision & " - " & myFile

    With cmbLiik
        .AddItem "Raamat"
        .ItemData(.NewIndex) = 1
        .AddItem "Õpik"
        .ItemData(.NewIndex) = 2
        .AddItem "Perioodika"
        .ItemData(.NewIndex) = 3
        .AddItem "Audio-Video"
        .ItemData(.NewIndex) = 4
        .AddItem "Töövihik"
        .ItemData(.NewIndex) = 5
        .AddItem "Metoodiline k."
        .ItemData(.NewIndex) = 6
        .ListIndex = 0
    End With
    
    FillSelected
    
    Exit Sub
Viga:
    If Err.Number = -2147217865 Then
        gRS.Open "CREATE TABLE MEEDIA_INVENTUUR (MEEDIA_INVENTUUR_ID COUNTER CONSTRAINT PrimaryKey PRIMARY KEY, MEEDIA_EKSEMPLAR_FK LONG, KOGUS LONG, KUUPAEV DATETIME DEFAULT Date())", gConnect
        GoTo Algus
    Else
        Err.Raise Err.Number, Err.Description
    End If
    
End Sub

Private Sub FillSelected()
    On Error GoTo Viga
    Dim mySQL As String
    Dim myName As String
    Dim myFile As String
    Dim a As String
    
Algus:
    
    mySQL = "SELECT MEEDIA_EKSEMPLAR.MEEDIA_EKSEMPLAR_ID, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER, MEEDIA.MEEDIA_LIIK, MEEDIA.PEALKIRI, MEEDIA.KLASS, MEEDIA.AUTOR, MEEDIA_INVENTUUR.KOGUS " _
           & "FROM  MEEDIA, MEEDIA_EKSEMPLAR, MEEDIA_INVENTUUR " _
           & "WHERE MEEDIA.MEEDIA_ID = MEEDIA_EKSEMPLAR.MEEDIA_FK " _
           & "AND MEEDIA_EKSEMPLAR.MEEDIA_EKSEMPLAR_ID = MEEDIA_INVENTUUR.MEEDIA_EKSEMPLAR_FK " _
           & "ORDER BY MEEDIA.MEEDIA_LIIK, MEEDIA.PEALKIRI, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER, MEEDIA.KLASS, MEEDIA.AUTOR"
           
    gRS.Open mySQL, gConnect
    Debug.Print mySQL
    
    lstSelected.Clear
    Do Until gRS.EOF
        myName = ""
        If LenB(Trim(gRS("MEEDIA_LIIK"))) > 0 Then myName = myName & Trim(gRS("MEEDIA_LIIK"))
        If LenB(Trim(gRS("INVENTARI_NUMBER"))) > 0 Then myName = myName & " " & Trim(gRS("INVENTARI_NUMBER")) & " -"
        If LenB(Trim(gRS("PEALKIRI"))) > 0 Then myName = myName & " " & Trim(gRS("PEALKIRI"))
        If LenB(Trim(gRS("KLASS"))) > 0 Then myName = myName & " " & Trim(gRS("KLASS"))
        If LenB(Trim(gRS("AUTOR"))) > 0 Then myName = myName & " (" & Trim(gRS("AUTOR")) & ")"
        If Trim(gRS("MEEDIA_LIIK")) <> "RA" And Trim(gRS("MEEDIA_LIIK")) <> "AV" Then myName = myName & " - " & Trim(gRS("KOGUS")) & "tk"
        
        lstSelected.AddItem myName
        lstSelected.ItemData(lstSelected.NewIndex) = gRS("MEEDIA_EKSEMPLAR_ID")
        gRS.MoveNext
    Loop
    lstSelected.Refresh
    
    gRS.Close
    
    Exit Sub
Viga:
    If Err.Number = -2147217865 Then
        gRS.Open "CREATE TABLE MEEDIA_INVENTUUR (MEEDIA_INVENTUUR_ID COUNTER CONSTRAINT PrimaryKey PRIMARY KEY, MEEDIA_EKSEMPLAR_FK LONG, KOGUS LONG, KUUPAEV DATETIME DEFAULT Date())", gConnect
        GoTo Algus
    Else
        Err.Raise Err.Number, Err.Description
    End If
End Sub




Private Sub btnSearch_Click()
    Dim mySQL As String
    Dim myWhere As String
    Dim myName As String
    
    myWhere = ""
    If IsNumeric(txtSearch.Text) Then
        myWhere = myWhere & "AND MEEDIA_EKSEMPLAR.INVENTARI_NUMBER = " & txtSearch.Text & " "
    Else
        myWhere = myWhere & "AND MEEDIA.PEALKIRI LIKE ""%" & txtSearch.Text & "%"" "
    End If
    
    Select Case cmbLiik.ItemData(cmbLiik.ListIndex)
        Case 1
            myWhere = myWhere & "AND MEEDIA.MEEDIA_LIIK = ""RA"" "
        Case 2
            myWhere = myWhere & "AND MEEDIA.MEEDIA_LIIK = ""OP"" "
        Case 3
            myWhere = myWhere & "AND MEEDIA.MEEDIA_LIIK = ""PE"" "
        Case 4
            myWhere = myWhere & "AND MEEDIA.MEEDIA_LIIK = ""AV"" "
        Case 5
            myWhere = myWhere & "AND MEEDIA.MEEDIA_LIIK = ""TV"" "
        Case 6
            myWhere = myWhere & "AND MEEDIA.MEEDIA_LIIK = ""MK"" "
        Case Else
            myWhere = myWhere & "AND 1=2 "
    End Select
    
    mySQL = "SELECT MEEDIA_EKSEMPLAR.MEEDIA_EKSEMPLAR_ID, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER, MEEDIA.MEEDIA_LIIK, MEEDIA.PEALKIRI, MEEDIA.KLASS, MEEDIA.AUTOR, MEEDIA_EKSEMPLAR.KOGUS " _
           & "FROM  MEEDIA, MEEDIA_EKSEMPLAR " _
           & "WHERE MEEDIA.MEEDIA_ID = MEEDIA_EKSEMPLAR.MEEDIA_FK " _
           & myWhere _
           & "ORDER BY MEEDIA.PEALKIRI, MEEDIA_EKSEMPLAR.INVENTARI_NUMBER, MEEDIA.KLASS, MEEDIA.AUTOR"
           
    gRS.Open mySQL, gConnect
    Debug.Print mySQL
    
    lstMedia.Clear
    Do Until gRS.EOF
        myName = ""
        If LenB(Trim(gRS("INVENTARI_NUMBER"))) > 0 Then myName = myName & gRS("INVENTARI_NUMBER") & " -"
        If LenB(Trim(gRS("PEALKIRI"))) > 0 Then myName = myName & " " & Trim(gRS("PEALKIRI"))
        If LenB(Trim(gRS("KLASS"))) > 0 Then myName = myName & " " & Trim(gRS("KLASS"))
        If LenB(Trim(gRS("AUTOR"))) > 0 Then myName = myName & " (" & Trim(gRS("AUTOR")) & ")"
        If Trim(gRS("MEEDIA_LIIK")) <> "RA" And Trim(gRS("MEEDIA_LIIK")) <> "AV" Then myName = myName & " - " & Trim(gRS("KOGUS")) & "tk"
        
        lstMedia.AddItem myName
        lstMedia.ItemData(lstMedia.NewIndex) = gRS("MEEDIA_EKSEMPLAR_ID")
        gRS.MoveNext
    Loop
    lstMedia.Refresh
    
    gRS.Close
    
    
End Sub




Private Sub Form_Resize()
    If Me.Height < 3000 Then Me.Height = 3000
    If Me.Width < 7000 Then Me.Width = 7000
        
    With lstMedia
        .Height = Me.Height - .Top - .Left * 5
        .Width = (Me.Width - frmButtons.Width) / 2 - .Left * 1.5
    End With
    With frmButtons
        .Top = (Me.Height / 2)
        .Left = lstMedia.Left + lstMedia.Width
    End With
    With lstSelected
        .Height = Me.Height - .Top - lstMedia.Left * 5
        .Left = frmButtons.Left + frmButtons.Width
        .Width = Me.Width - .Left - lstMedia.Left * 2
    End With
    lblSelected.Left = frmButtons.Left + frmButtons.Width
    
    txtSearch.Width = lstMedia.Width - txtSearch.Left - btnSearch.Width
    btnSearch.Left = txtSearch.Width + txtSearch.Left + lstMedia.Left
    
    btnPrint.Left = Me.Width - btnPrint.Width - lstMedia.Left * 2

    
End Sub

Private Sub lstMedia_DblClick()
    btnSelect_Click
End Sub

Private Sub btnSelect_Click()
    Dim myID As Long
    Dim myKogus
    
    If lstMedia.ListIndex < 0 Then Exit Sub
    
    With lstMedia
        myID = .ItemData(.ListIndex)
        .RemoveItem .ListIndex
    End With
    
    gRS.Open "DELETE FROM MEEDIA_INVENTUUR WHERE MEEDIA_EKSEMPLAR_FK = " & myID
    
    myKogus = 1
    If cmbLiik.ItemData(cmbLiik.ListIndex) <> 1 And cmbLiik.ItemData(cmbLiik.ListIndex) <> 4 Then
        gRS.Open "SELECT * FROM MEEDIA_EKSEMPLAR WHERE MEEDIA_EKSEMPLAR_ID = " & myID
        gRS.MoveFirst
        myKogus = InputBox("Mitu eksemplari olemas on?", , gRS("KOGUS"))
        gRS.Close
        If IsNumeric(myKogus) = False Then Exit Sub
        If myKogus < 1 Then Exit Sub
    End If
    
    gRS.Open "INSERT INTO MEEDIA_INVENTUUR (MEEDIA_EKSEMPLAR_FK, KOGUS) VALUES (" & myID & ", " & myKogus & ")"
    
    FillSelected

End Sub




Private Sub lstSelected_DblClick()
    btnDeselect_Click
End Sub

Private Sub btnDeselect_Click()
    Dim myID As Long
    Dim myText As String
    
    If lstSelected.ListIndex < 0 Then Exit Sub
    If MsgBox("Olete kindel et soovite teaviku eemaldada?", vbQuestion + vbYesNo) = vbNo Then Exit Sub
    
    
    
    
    With lstSelected
        myID = .ItemData(.ListIndex)
        myText = .Text
        .RemoveItem .ListIndex
        gRS.Open "DELETE FROM MEEDIA_INVENTUUR WHERE MEEDIA_EKSEMPLAR_FK = " & myID
    End With
    
    With lstMedia
        .AddItem myText
        .ItemData(.NewIndex) = myID
    End With
End Sub
